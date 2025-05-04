from django.shortcuts import render
from .forms import ProductComparisonForm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib import messages
from comparing.models import Contact
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from comparing.forms import CustomUserCreationForm 

# Create your views here.

def index(request):
    # Render the About page template with context (if needed)
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Login attempt: username={username}, password={'*' * len(password)}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User authenticated successfully")
            login(request, user)
            return redirect('services')
        else:
            print("Authentication failed")
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def logout_view(request):
    logout(request) 
    return redirect('index')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Make sure this line is present
            login(request, user)
            return redirect('services')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def services(request):
    comparison_result = None
    if request.method == "POST":
        form = ProductComparisonForm(request.POST)
        if form.is_valid():
            url1 = form.cleaned_data['product1']
            url2 = form.cleaned_data['product2']
            comparison_result = compare_products(url1, url2)
        else:
            messages.error(request, 'Invalid form submission')
            return redirect('services')  # Adjust to a valid URL
    else:
        form = ProductComparisonForm()
    
    return render(request, 'services.html', {'form': form, 'comparison_result': comparison_result})


def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_product(url):
    driver = setup_driver()
    try:
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        title = wait.until(EC.presence_of_element_located((By.ID, 'productTitle'))).text.strip()

        imgcont = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#imgTagWrapperId')))
        photo = imgcont.find_element(By.TAG_NAME,'img').get_attribute('src')

        price_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#apex_desktop')))
        amount = price_element.find_element(By.CSS_SELECTOR, '.a-price-whole').text
        symbol = price_element.find_element(By.CSS_SELECTOR,'.a-price-symbol').text
        price = f"{symbol}{amount}"

        # Add the new product details scraping
        product_info = driver.find_element(By.CSS_SELECTOR, '#productDetails_feature_div')
        features = product_info.find_elements(By.CSS_SELECTOR, '.prodDetSectionEntry')
        values = product_info.find_elements(By.CSS_SELECTOR, '.prodDetAttrValue')

        details = {}
        for feature, value in zip(features, values):
            details[feature.text.strip()] = value.text.strip()

        return {'photo': photo, 'title': title, 'price': price, 'details': details}
    except Exception as e:
        return {'photo': 'Error', 'title': 'Error', 'price': 'Error', 'details': {}, 'error': str(e)}
    finally:
        driver.quit()

def compare_products(url1, url2):
    product1 = scrape_product(url1)
    product2 = scrape_product(url2)

    return {
        'product1': product1,
        'product2': product2
    }

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Profile details updated.")
    return render (request,'contact.html')
