# Add documentation link
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class LMS(models.Model):
	name = models.CharField(max_length=128)
	url = models.CharField(max_length=128)

	class Meta:
		verbose_name = 'LMS'
		verbose_name_plural = 'LMS'

	def __unicode__(self):
		return self.name

class LMS_Web_Service(models.Model):
	web_service_name = models.CharField(max_length=128)
	# depending on the options we might be able to do a choicefield here
	web_service_method = models.CharField(max_length=128)
	web_service_url = models.CharField(max_length=128)

	class Meta:
		verbose_name = 'LMS Web Service'
		verbose_name_plural = 'LMS Web Services'

	def __unicode__(self):
		return self.web_service_name

class School(models.Model):
	lms = models.ForeignKey(LMS, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	url = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name

# Not the most creative person. Please find a better name :)
# Also depending on our needs (i.e. we might have to use a custom user model)
class My_User(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	lms = models.ForeignKey(LMS, on_delete=models.CASCADE)
	email = models.CharField(max_length=128)

	class Meta:
		verbose_name = 'FAL User'
		verbose_name_plural = 'FAL Users'

# TODO: Find out why there are 3 sss
class Class(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	lms = models.ForeignKey(LMS, on_delete=models.CASCADE)
	my_user = models.ForeignKey(My_User, on_delete=models.CASCADE, related_name='Teacher')
	name = models.CharField(max_length=128)
	# based on our needs, this might be a choicefield
	academic_year = models.IntegerField()
	# based on our needs, this might be a choicefield, or even integer (wasn't sure of the options)
	semester = models.CharField(max_length=128)

	# class Meta:
	# 	verbose_name = 'FAL Class'
	# 	verbose_name_plural = 'FAL Classes'

class Assignment(models.Model):
	name = models.CharField(max_length=128)

class Question(models.Model):
	name = models.CharField(max_length=128)
	# This is assuming that only Students can ask questions
	# Please note that related_name is simply for display and does not affect the db in any given way
	my_user = models.ForeignKey(My_User, on_delete=models.CASCADE, related_name='Student')

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, )
	name = models.CharField(max_length=128)
	# Same comment Question.my_user applies here
	my_user = models.ForeignKey(My_User, on_delete=models.CASCADE, related_name='Provided By+')


class Video(models.Model):
	name = models.CharField(max_length=128)
	location = models.CharField(max_length=128)

class Video_Comment(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='Student')
	my_user = models.ForeignKey(My_User, on_delete=models.CASCADE, related_name='Commenter')
	# Actual lenght might have to be changed
	comment = models.CharField(max_length=128)

class Interview(models.Model):
	name = models.CharField(max_length=128)
	my_user = models.ForeignKey(My_User, on_delete=models.CASCADE, related_name='Student')
	my_user = models.ForeignKey(My_User, on_delete=models.CASCADE, related_name='Professional')
	date = models.DateTimeField()