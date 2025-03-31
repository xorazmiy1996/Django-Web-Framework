from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='', required=False,
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search recipes...'}))
