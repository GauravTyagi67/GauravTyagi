from content.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    fullname = forms.CharField(required=True,max_length=100)
    email = forms.EmailField(required=True,max_length=254)
    subject = forms.CharField(required=True,max_length=200)
    phone_number = forms.CharField(required=True,max_length=15)
    message = forms.CharField(required=True,widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = [
            'fullname',
            'email',
            'subject',
            'message',
            'phone_number',
        ]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs['placeholder'] = 'Your FullName'
        self.fields['fullname'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Your Contact Number'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['placeholder'] = 'Your Subject'
        self.fields['subject'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message'
        self.fields['message'].widget.attrs['cols'] = '30'
        self.fields['message'].widget.attrs['rows'] = '10'