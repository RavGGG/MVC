from django import forms
from .models import Book
import datetime
import re

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if re.search(r'\d', author):
            raise forms.ValidationError("Author name cannot contain digits.")
        return author

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        current_year = datetime.datetime.now().year
        if year > current_year:
            raise forms.ValidationError("Year cannot be in the future.")
        if year < 1000 or year > 9999:
            raise forms.ValidationError("Year must be a 4-digit number.")
        return year
