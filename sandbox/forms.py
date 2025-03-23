from django import forms

from sandbox.models import Feedback

choice = [
    ("happy", "Happy"),
    ("neutral", "Neutral"),
    ("sad", "Sad"),
]

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    feedback = forms.CharField( label='Your feedback', widget=forms.Textarea)
    satisfied = forms.ChoiceField(choices=choice, widget=forms.RadioSelect)

