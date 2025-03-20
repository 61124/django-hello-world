# example/views.py
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    now = datetime.now()
    context = {
        'current_time': now,
    }
    return render(request, 'example/index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # In a real application, you might send an email here
            # or save the message to a database
            
            # Redirect to a thank you page or back to the form with a success message
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'example/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'example/contact_success.html')
