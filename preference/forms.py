from django import forms
from .models import Preference

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = '__all__'
        
    def clean_bio(self):
        bio = self.cleaned_data['bio']
        if len(bio) > 500:
            raise forms.ValidationError('Bio should not be more than 500 characters')
        elif len(bio) < 10:
            raise forms.ValidationError('Bio should be at least 10 characters long')
        
        return bio
    
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 2:
            raise forms.ValidationError('Name should be at least 2 characters long')
        
        return first_name