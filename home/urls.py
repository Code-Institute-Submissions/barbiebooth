from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
]
