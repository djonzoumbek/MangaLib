from django import forms
from .models import Author, Book


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Author')
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity']
        labels = {'title': 'Title', 'author': 'Author', 'quantity': 'Quantity'}


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'