from django import forms

from comments.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control','rows':'2'}),
        }