from django.urls import path
from comparing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('services/', views.services, name='services'),
    path("contact",views.contact,name='contact'),
]