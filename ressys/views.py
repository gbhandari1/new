from django.shortcuts import render, redirect
from ressys.models import *
from ressys.forms import ApplicantForm, CreateUserForm
from django.urls import reverse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView, UpdateView,DeleteView)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_users, admin_only
# Create your views here.

@login_required(login_url = 'ressys:login_user')
@admin_only
def HomeView(request):
    applicants = Applicant.objects.all()
    context = {'applicants': applicants}
    return render (request,'applicant_list.html', context)

@login_required(login_url = 'ressys:login_user')
def createApplicantView (request):
    form = ApplicantForm()
    if request.method == 'POST':
        form = ApplicantForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render (request, 'applicant_form.html', context)

@login_required(login_url = 'ressys:login_user')
def applicantDetailView(request, pk):
    applicant =  Applicant.objects.get(id=pk)
    context = {'applicant':applicant}
    return render (request, 'applicant_detail.html',context)

@login_required(login_url = 'ressys:login_user')
def applicantUpdateView(request,pk):
    applicant = Applicant.objects.get (id=pk)
    form = ApplicantForm(instance=applicant)
    if request.method == 'POST':
        form = ApplicantForm(request.POST, instance=applicant)

        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render (request, 'applicant_form.html', context)

@login_required(login_url = 'ressys:login_user')
def applicantDeleteView(request,pk):
    applicant = Applicant.objects.get (id=pk)
    if request.method == 'POST':
        applicant.delete()
        return redirect('/')
    context = {'applicant':applicant}
    return render(request,'delete.html',context)

def registerView (request):
    if request.user.is_authenticated:
        return redirect('ressys:home')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name = 'customers')
                user.groups.add(group)
                messages.success(request,'Account was created for ' + username )
                return redirect('ressys:login_user')
        context = {'form': form}
        return render (request,'registration.html',context)


@unauthenticated_user
def loginView (request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username , password = password)

            if user is not None:
                login(request,user)
                return redirect('ressys:home')
            else :
                messages.info(request,'Username or Password is Incorrect.')
        return render (request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('ressys:login_user')

def userView(request):
    context ={}
    return render (request, 'user.html', context)
