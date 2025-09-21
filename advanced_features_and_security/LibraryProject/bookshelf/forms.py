from django import forms
from .models import Book

class Book(forms.ModelForm):
    """Form for validating ExampleModel input safely."""
    
    class Meta:
        model = Book
        fields = ['owner']   # Add other model fields if required

    # Custom validation example
    def clean_owner(self):
        owner = self.cleaned_data.get('owner')
        if not owner:
            raise forms.ValidationError("Owner field cannot be empty.")
        return owner
