from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from models import *
from django.core.mail import send_mail
from django.conf import settings
import string
import random
import pdf
from cStringIO import StringIO
from reportlab.pdfgen import canvas
# Create your views here.
data = {}
def home(request):
    print request.META['HTTP_USER_AGENT']
    if "IE" in request.META['HTTP_USER_AGENT']:
        return render(request,'warning.html',{})
    return render(request, 'index.html', {})

def mail(request):
	client_ip = request.META["REMOTE_ADDR"]
	print client_ip
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

	text="Submit the change of discipline form by clicking this link: http://10.1.1.239/form/"+key+"/"
	send_mail('Course Change Portal', text, settings.EMAIL_HOST_USER, [request.POST['email']], fail_silently=False)
	return HttpResponse("<b>An email has been sent to your email address.Please Follow the link in the email</b>")

def form(request,key):
    try:
        p = Student.objects.get(key=key)
        if p.flag == 0:
            return render(request,'form.html',{'p':p})
        else:
            return render(request,'registered.html',{'p':p})
    except:
        return HttpResponse("Invalid link")

def submit(request,key):
	if request.method=="POST":
		try:
			s = Student.objects.get(key=key)
		except:
			return HttpResponse("Validation failed.")
		else:
			temp = StringIO()
			p = canvas.Canvas(temp)
			response = HttpResponse(content_type = 'application/pdf')
			response['Content-Disposition'] = 'attachment;filename=Branch_Change_Form.pdf'
			s.name = request.POST["name"]
			data["name"] = s.name
			s.air = request.POST["air"]
			data["air"] = s.air
			s.roll = request.POST["roll"]
			data["roll"] = s.roll
			s.ptype = request.POST["ptype"]
			data["ptype"] = s.ptype
			s.branch = request.POST["branch"]
			data["branch"] = s.branch
			s.choice1 = request.POST["choice1"]
			data["choice1"] = s.choice1
			s.choice2 = request.POST["choice2"]
			data["choice2"] = s.choice2
			s.choice3 = request.POST["choice3"]
			data["choice3"] = s.choice3
			s.choice4 = request.POST["choice4"]
			data["choice4"] = s.choice4
			s.choice5 = request.POST["choice5"]
			data["choice5"] = s.choice5
			s.spi1 = request.POST["spi1"]
			s.flag = 1
			data["key"]=key
			data["spi1"] = s.spi1
			data["email"] = s.email
			p = pdf.pdf_gen(p,data)
			p.showPage()
			p.save()
			s.save()
			response.write(temp.getvalue())
			return render(request,'download.html',data)           


	else:
		return HttpResponse("Validation failed.")
def pdf_download(request,key):
    s = Student.objects.get(key=key)
    data["name"] = s.name
    data["air"] = s.air
    data["roll"] = s.roll
    data["ptype"] = s.ptype
    data["branch"] = s.branch
    data["choice1"] = s.choice1
    data["choice2"] = s.choice2
    data["choice3"] = s.choice3
    data["choice4"] = s.choice4
    data["choice5"] = s.choice5
    data["spi1"] = s.spi1
    data["email"] = s.email
    temp = StringIO()
    p = canvas.Canvas(temp)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=Branch_Change_Form.pdf'
    p = pdf.pdf_gen(p,data)
    p.showPage()
    p.save()
    response.write(temp.getvalue())
    return response

