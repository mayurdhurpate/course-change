from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.core.mail import send_mail
from django.conf import settings
import string
import random
# Create your views here.

def home(request):
	return render(request, 'index.html', {})

def mail(request):
	email = request.POST["email"]
	try:
		p = Student.objects.get(email=email)
		key = p.key
	except:
		p = Student()
		key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)) 
		p.email = email
		p.key = key

		p.save()
	print key

	text="Submit the course change form by clicking this link: http://localhost:8000/form/"+key+"/" 
	#send_mail('Course Change Portal', text, settings.EMAIL_HOST_USER, [request.POST['email']], fail_silently=False)
	return HttpResponse("An email has been sent to your email address.")

def form(request,key):
	try:
		p = Student.objects.get(key=key)
		return render(request, 'form.html', {'p':p})
	except:
		return HttpResponse("Invalid Link")

def submit(request,key):
	if request.method=="POST":
		try:
			s = Student.objects.get(key=key)
		except:
			return HttpResponse("Validation failed.")
		else:
			s.name = request.POST["name"]
			s.air = request.POST["air"]
			s.roll = request.POST["roll"]
			s.ptype = request.POST["ptype"]
			s.branch = request.POST["branch"]
			s.choice1 = request.POST["choice1"]
			s.choice2 = request.POST["choice2"]
			s.choice3 = request.POST["choice3"]
			s.choice4 = request.POST["choice4"]
			s.choice5 = request.POST["choice5"]
			s.save()
			return HttpResponse("Form Submitted...")
	else:
		return HttpResponse("Validation failed.")