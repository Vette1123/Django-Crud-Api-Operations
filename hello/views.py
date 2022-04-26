from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Track
from . forms import StudentForm, UserForm


# rest_framework api imports here

from .serializers import StudentSerializer, TrackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# ouath imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Ouath views here

def signIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            userName = request.POST.get('username')
            userPassword = request.POST.get('password')
            user = authenticate(username=userName, password=userPassword)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
            else:
                messages.info(request, 'User name or password is incorrect')
        return render(request, 'hello/login.html')


def signUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form = UserForm()
        if(request.method == 'POST'):
            signup_form = UserForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + \
                    signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
        context = {'signup_form': signup_form}
        return render(request, 'hello/signup.html', context)


def signOut(request):
    logout(request)
    return redirect('login')

# rest_framework api views here


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

@login_required(login_url='login')
def home(request):
    all_students = Student.objects.all()
    # context variable is a dictionary, 3rd param
    context = {'all_students': all_students}
    return render(request, 'hello/home.html', context)


@login_required(login_url='login')
def show(request, std_id):
    student = Student.objects.get(id=std_id)
    context = {'student': student}
    return render(request, 'hello/show.html', context)

@login_required(login_url='login')
def delete_student(request, std_id):
    student = Student.objects.get(id=std_id)
    student.delete()
    return redirect('home')

@login_required(login_url='login')
def add_student(request):
    std_form = StudentForm()
    if request.method == 'POST':
        std_form = StudentForm(request.POST)
        if std_form.is_valid():
            std_form.save()
            return redirect('home')
    context = {'std_form': std_form}
    return render(request, 'hello/add.html', context)

@login_required(login_url='login')
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


