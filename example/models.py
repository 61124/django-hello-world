# example/models.py
from django.db import models
from django.utils import timezone

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.subject} - {self.name}"
    
    class Meta:
        ordering = ['-created_at']
