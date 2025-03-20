# example/views.py
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import ContactSubmission

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
            # Save the form data to the database
            submission = ContactSubmission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            submission.save()
            
            # Redirect to success page
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'example/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'example/contact_success.html')

@login_required
def submission_list(request):
    submissions = ContactSubmission.objects.all()
    return render(request, 'example/submission_list.html', {'submissions': submissions})

@login_required
def submission_detail(request, submission_id):
    submission = ContactSubmission.objects.get(id=submission_id)
    return render(request, 'example/submission_detail.html', {'submission': submission})
