from django.shortcuts import render, redirect
from .models import Doctors, Contacts, Appointment,Testimonials
from datetime import datetime
# Create your views here.

def index(request):
    context = {
        "expert_doctors" : 30,
        "staff": 60,
        "patients": 800,

        "doctors" : Doctors.objects.all(),
        "testimonials" : Testimonials.objects.all()
    }
    return render(request, 'index.html',context)

def about(request):
    context = {
        "doctors" : Doctors.objects.all()
    }
    return render(request,'about.html',context)

def service(request):
    context = {
        "testimonials" : Testimonials.objects.all()
    }
    return render(request, 'service.html', context)

def team(request):
    context = {
        "doctors" : Doctors.objects.all()
    }
    return render(request, 'team.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new_contact = Contacts.objects.create(name = name, email = email, subject = subject, message = message)

        return redirect('contact')
    return render(request, 'contact.html')

def appointment(request):

    context = {
        "doctors" : Doctors.objects.all(),
        "appointments" : Appointment.objects.all()          
    }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        doctor = request.POST['doctor']
        date = datetime.strptime(request.POST['date'],'%m/%d/%Y')
        time = datetime.strptime(request.POST['time'],'%I:%M %p').time()
        problem = request.POST['problem']

        isBooked = False

        if Appointment.objects.filter(doctor = doctor, date = date, time = time).exists():
            data_exists = True
            
        else:
            data_exists = False
            new_appointment = Appointment.objects.create(name = name, email = email, mobile = mobile, doctor = doctor, date = date, time = time, problem = problem)
            isBooked = True
            return redirect('appointment')
        
        context.update({'data_exists' : data_exists, 'isBooked' : isBooked})

    return render(request,'appointment.html', context)

