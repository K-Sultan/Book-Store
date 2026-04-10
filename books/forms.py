from django import forms
from .models import Book
from authors.models import Author


class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    breif = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    no_of_page = forms.IntegerField(min_value=1)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        required=False
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title.strip()) < 2:
            raise forms.ValidationError('Title must be at least 2 characters.')
        return title

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price