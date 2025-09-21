# LibraryProject/bookshelf/forms.py
from django import forms
from .models import ExampleModel   # ✅ make sure ExampleModel exists in models.py

class ExampleForm(forms.ModelForm):
    """Form for validating ExampleModel input safely."""
    
    class Meta:
        model = ExampleModel
        fields = ['owner']   # Add other fields from ExampleModel if required

    # Custom validation example
    def clean_owner(self):
        owner = self.cleaned_data.get('owner')
        if not owner:
            raise forms.ValidationError("Owner field cannot be empty.")
        return owner
