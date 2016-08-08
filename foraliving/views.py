# from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import loader
# from .forms import *
from .models import *
# from .filters import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def index(request):
	return render(request,'homepage.html') 

def twopage(request):
	return render(request,'home.html') 
