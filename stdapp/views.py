from django.shortcuts import render, redirect
from django.http import HttpResponse
from stdapp.forms import StudentForm
from django.urls import reverse
from django.contrib import messages

from .models import Student
from .models import Person
# Create your views here.

def index(request):
    return render(request, 'index.html')
def save(request):
    return render(request, 'save.html')
def edit(request):
    return render(request, 'edit.html')

def std(request):
    all_student = Student.objects.all()
    return render(request,'student.html',{'all_student':all_student})

def person(request):
    all_person = Person.objects.all()
    return render(request,'person.html',{'all_person':all_person})

def form_view(request):
    if request.method == 'POST':
        pname = request.POST["pname"]
        page = request.POST["page"]
        pdepartment = request.POST["pdepartment"]
        new_person = Person.objects.create(pname=pname, page=page, pdepartment=pdepartment)
        new_person.save()
        return redirect(reverse('person'))
    else:
        return render(request,'form_view.html')
    
def delete(request, person_id):
    delete_person = Person.objects.get(id=person_id)
    delete_person.delete()
    messages.error(request, "ลบข้อมูลเรียบร้อย")
    return redirect(reverse('person'))

def edit(request, person_id):
        return render(request,'edit.html')

def edit(request, person_id):
    if request.method == 'POST':
        person = Person.objects.get(id=person_id)
        person.pname = request.POST["pname"]
        person.page = request.POST["page"]
        person.pdepartment = request.POST['pdepartment']
        person.save()
        messages.success(request,"แก้ไขข้อมูลเรียบร้อย")
        return redirect(reverse('person')) 
    else :
        person = Person.objects.get(id=person_id)
        return render(request,'edit.html', {'person' : person })
