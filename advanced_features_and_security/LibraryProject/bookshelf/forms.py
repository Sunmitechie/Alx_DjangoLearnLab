from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100)        