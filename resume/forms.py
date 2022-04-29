from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

		widgets = {
		'name':  forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Name'}),
		'email':forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'placeholder':'Email Address'}),
		'phone': forms.TextInput(attrs={'class':'form-control', 'id':'phone', 'placeholder':'Phone number'}),
		'text':   forms.Textarea(attrs={'class':'form-control', 'id':'message', 'placeholder':'Message'}),
		}