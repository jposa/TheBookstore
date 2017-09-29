from django import forms


class ContactForm(forms.Form):
    from_ = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)