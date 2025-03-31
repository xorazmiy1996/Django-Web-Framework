from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_photo')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 80}),
            'profile_photo': forms.ClearableFileInput(attrs={'class':'form-control','multiple': False}),
        }