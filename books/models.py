from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    breif = models.TextField()
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    no_of_page = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    authors = models.ManyToManyField('authors.Author', related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 