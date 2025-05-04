# AmazonCompareIT

AmazonCompareIT is a modern Django web application that allows users to compare Amazon products side-by-side by simply pasting product URLs. The app scrapes product details and presents them in a beautiful, user-friendly interface.

## Features
- **Amazon Product Comparison:** Enter two Amazon product URLs and get a detailed, side-by-side comparison of images, prices, and features.
- **User Authentication:** Register, login, and logout with a custom user model.
- **Contact Form:** Users can send messages via a contact form.
- **Modern UI:** Responsive, aesthetic design using Bootstrap 5 and custom CSS.
- **Selenium Integration:** Uses Selenium and ChromeDriverManager for scraping product data.

## Project Structure
```
├── amazonCompareIT/        # Django project settings and URLs
├── comparing/             # Main app: models, views, forms, templates
├── static/                # Custom CSS and static assets
├── templates/             # HTML templates
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore file
└── README.md              # Project documentation
```

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd amazoncompareit
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the app:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage
- **Compare Products:** Go to the Services page, paste two Amazon product URLs, and click Compare.
- **Register/Login:** Create an account or log in to access comparison features.
- **Contact:** Use the contact form to send a message to the site owner.

## Notes
- **Selenium:** The app uses Selenium and ChromeDriverManager. Chrome must be installed on your system.
- **Static Files:** Custom CSS is in `static/css/style.css`.

## License
This project is for educational/demo purposes.

---
**Made with ❤️ by Subrato Singh & his partner Sanidhya Patel (CSS)** 