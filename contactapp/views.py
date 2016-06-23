from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

# Create your views here.


def contact(request):
	form = ContactForm
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			subject = request.POST.get('subject', '')
			content = request.POST.get('content', '')

			#Email the profile with conatct information

			template = get_template('contact_template.txt')
			context = Context({'contact_name':contact_name, 'contact_email':contact_email, 'subject':subject, 'content':content,})
			content_info = template.render(context)

			email = EmailMessage(
				subject, content,
				contact_name+'<%s>' % contact_email, ['thestartech.amitsin6h@gmail.com'],
				headers = {'Reply-To': contact_email}
				)
			email.send()
			return HttpResponse('Your Message is sent successfully!!') 	

	return render(request, 'index.html', {'form':form})