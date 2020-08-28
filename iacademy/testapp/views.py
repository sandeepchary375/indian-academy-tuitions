from django.shortcuts import render
from .models import Tutors, Students
# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contactus.html')


def gallery_view(request):
    return render(request, 'gallery.html')


def register_view(request):
    return render(request, 'register.html')


def tutor_register(request):
    if request.method == 'POST':
        name = request.POST['t1']
        cellno = request.POST['t2']
        email = request.POST['t3']
        tr = Tutors(name1=name, cellno1=cellno, email1=email)
        tr.save()

    return render(request, 'tutor.html')


def student_register(request):
    if request.method == 'POST':
        name = request.POST['t1']
        fathername = request.POST['t2']
        area = request.POST['t3']
        cellno = request.POST['t4']
        email = request.POST['t5']
        address = request.POST['t6']
        sv = Students(name1=name, fathername1=fathername, area1=area, cellno1=cellno, email1=email, addres1=address)
        sv.save()
    return render(request, 'student.html')

