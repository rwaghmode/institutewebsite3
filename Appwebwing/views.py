from django.shortcuts import render,redirect
from .models import StudentContact
# Create your views here.
def home(request):
    return render(request,template_name='home.html')


def about(request):
    return render(request,template_name='aboutus.html')


def courses(request):
    return render(request,template_name='courses.html')


# def pricing(request):
#     return render(request,template_name='pricing.html')
def contact(request):
    return render(request, template_name='contact.html')

def placement(request):
    return render(request,template_name='placement.html')

def contact_save(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    student_contact = StudentContact()
    student_contact.name = name
    student_contact.email = email
    student_contact.subject = subject
    student_contact.message = message
    student_contact.save()
    return redirect('contact')