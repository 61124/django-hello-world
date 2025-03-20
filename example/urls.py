# example/urls.py
from django.urls import path
from example.views import index, contact, contact_success

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]
