# pylint: disable=import-error
"""Contacts admin"""
from datetime import datetime
from django.db import models


# Create your models here.
class Contact(models.Model):
    """Contact model"""
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
