from django import forms
from .models import Contact

class ContactForm(forms.Form):
    conName = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form__input'}))
    conEmail = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class': 'form__input'}))
    conMessage = forms.CharField(label='How can help you?', widget=forms.Textarea(attrs={'id': 'message'}))

    class Meta:
        model = Contact
        fields = ('Name','Email', 'Message')