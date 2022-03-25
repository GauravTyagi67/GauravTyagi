from content.forms import ContactForm
from django.shortcuts import render
from content.models import Profile, About, PrimarySkill, SecondarySkill, Service, Portfolio, Blog, Testimonial
#from content.models import *

#for sending email function
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.template import loader
from django.contrib import messages

# Create your views here.
def Homepage(request):
	profile=Profile.objects.first()
	about=About.objects.first()
	primary_skill=PrimarySkill.objects.all()
	secondary_skill=SecondarySkill.objects.all()
	service= Service.objects.all()
	portfolio=Portfolio.objects.all()
	blog=Blog.objects.all()
	testimonial=Testimonial.objects.all()
	form=ContactForm()
	context={
		'profile':profile,
		'about':about,
		'skill1':primary_skill,
		'skill2':secondary_skill,
		'service':service,
		'portfolio':portfolio,
		'blog':blog,
		'testimonial':testimonial,
		'form':form,
	}
	return render(request,"index.html",context)


def MailContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.fullname = form.cleaned_data['fullname']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.phone_number = form.cleaned_data['phone_number']
            data.message = form.cleaned_data['message']
            data.save()
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            fullname = form.cleaned_data['fullname']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['gktyagi2018@gmail.com',]
            html_message = loader.render_to_string(
                'email.html',
                {
                    'subject':subject,
                    'message':message,
                    'fullname':fullname,
                    'email':email,
                    'phone_number':phone_number,
                }
            )
            if subject and message and email_from and recipient_list and html_message:
                try:
                    send_mail(subject, message, email_from, recipient_list, html_message = html_message, fail_silently=False)
                except:
                    messages.error(request,"Cannot send mail right now, Try again later")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                messages.success(request,"Message sent successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request,"Please! Make sure all fields are entered and valid.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request,"Please! Make sure all fields are entered and valid.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))