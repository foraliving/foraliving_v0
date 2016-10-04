from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import loader
from .forms import *
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def index(request):
	videoDemo = Video.objects.filter(tags__contains='homepage', tags__icontains='demo')
	videos = Video.objects.filter(tags__contains='homepage', ).exclude(tags__icontains='demo')
	return render(request,'homepage.html', {'videos' : videos, 'videoDemo' : videoDemo, }) 

def twopage(request):
	return render(request,'home.html') 

def sitetheme(request):
	return render(request,'FAL_Theme.html') 

def interviewSetup(request):
	return render(request, 'interview_setup.html')

def record(request):
	return render(request, 'record.html')

def volunteerSignup(request):
	if request.method == 'POST':
		userForm = volunteerUserSignupForm(request.POST)
		infoForm = volunteerSignupForm(request.POST)
		if userForm.is_valid():
			userForm.save()
		return redirect('record')
	else:
		userForm = volunteerUserSignupForm()
		infoForm = volunteerSignupForm()
		
	return render(request, 'volunteer_signup.html', {'userForm': userForm, 'infoForm': infoForm}, )