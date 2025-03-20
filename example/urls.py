# example/urls.py
from django.urls import path
from example.views import index, contact, contact_success, submission_list, submission_detail

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('submissions/', submission_list, name='submission_list'),
    path('submissions/<int:submission_id>/', submission_detail, name='submission_detail'),
]
