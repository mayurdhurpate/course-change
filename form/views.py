from django.shortcuts import render
from django.http import HttpResponse
from models import *


# Create your views here.
def home(request):
	return render(request, 'index.html', {})

def submit(request):
	s = Student()
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
	s.cpi1 = request.POST["cpi1"]
	s.save()
	return HttpResponse("Form Submitted...")