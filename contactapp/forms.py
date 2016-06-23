from django import forms

# contact form
class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Full Name..'}))
	contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email...'}))
	subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Subject...'}))
	content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Message...'}))

	