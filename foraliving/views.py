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

# Please remember to add login decorator if the view is login required

@login_required
def home(request):
	return render_to_response('homepage.html')