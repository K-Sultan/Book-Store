from django.db import models

# Create your models here.
class Author(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    GENDER_CHOICES =  models.CharField(max_length=1,choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name