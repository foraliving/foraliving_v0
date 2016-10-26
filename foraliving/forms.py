from django import forms
from .models import *
from django.contrib.auth.models import User, Group

class volunteerUserSignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password', ]
class volunteerSignupForm(forms.ModelForm):
	class Meta:
		model = Volunteer_User_Add_Ons
		# fields = '__all__'
		exclude = ['user']

class newSkillForm(forms.ModelForm):
	class meta:
		model = Skill

class newInterestForm(forms.ModelForm):
	class meta:
		model = Skill