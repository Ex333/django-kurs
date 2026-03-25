from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100, label="Imię")
    email = forms.EmailField(label="Email")
    text = forms.CharField(
        widget=forms.Textarea,
        min_length=10,
        label="Wiadomość"
    )