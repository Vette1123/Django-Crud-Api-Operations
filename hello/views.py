from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Track
from . forms import StudentForm


#rest_framework api imports here

from .serializers import StudentSerializer, TrackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

#rest_framework api views here

@api_view(['GET'])
def api_all_student(request):
    all_students = Student.objects.all()
    serializer = StudentSerializer(all_students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_one_student(request, std_id):
    student = Student.objects.get(id=std_id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['POST'])
def api_add_student(request):
    std_ser = StudentSerializer(data=request.data)
    if std_ser.is_valid():
        std_ser.save()
        return redirect('api-all')

@api_view(['POST'])
def api_edit_student(request, std_id):
    student = Student.objects.get(id=std_id)
    std_ser = StudentSerializer(instance=student, data=request.data)
    if std_ser.is_valid():
        std_ser.save()
        return redirect('api-all')
@api_view(['DELETE'])       
def api_delete_student(request, std_id):
    student = Student.objects.get(id=std_id)
    student.delete()
    return Response("Student Deleted")

# Create your views here.

def home(request):
    all_students = Student.objects.all()
    # context variable is a dictionary, 3rd param
    context = {'all_students': all_students}
    return render(request, 'hello/home.html', context)


def show(request, std_id):
    student = Student.objects.get(id=std_id)
    context = {'student': student}
    return render(request, 'hello/show.html', context)


def delete_student(request, std_id):
    student = Student.objects.get(id=std_id)
    student.delete()
    return redirect('home')


def add_student(request):
    std_form = StudentForm()
    if request.method == 'POST':
        std_form = StudentForm(request.POST)
        if std_form.is_valid():
            std_form.save()
            return redirect('home')
    context = {'std_form': std_form}
    return render(request, 'hello/add.html', context)

def edit_student(request, std_id):
    student = Student.objects.get(id=std_id)
    std_form = StudentForm(instance=student)
    if request.method == 'POST':
        std_form = StudentForm(request.POST, instance=student)
        if std_form.is_valid():
            std_form.save()
            return redirect('home')
    context = {'std_form': std_form}
    return render(request, 'hello/add.html', context)