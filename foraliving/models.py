# Add documentation link
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
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


class User_Add_Ons(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	# The user's ID w/in their LMS
	lms = models.ForeignKey(LMS, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'User Add-ons'
		verbose_name_plural = 'User Add-ons'

	def __unicode__(self):
		return self.user

class Group(models.Model):
	name = models.CharField(max_length=128)

class User_Group_Map(models.Model):
	# group = 
	user = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE)
	# To be defined
	# roles = (
	# 	(''),
	# 	(''),)
	# user_role =  models.CharField(max_length=1, choices=roles)

class Class(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	lms = models.ForeignKey(LMS, on_delete=models.CASCADE)
	teacher = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, )
	name = models.CharField(max_length=128)
	academic_year = models.IntegerField()
	semester = models.CharField(max_length=128)

	class Meta:
		verbose_name = 'FAL Class'
		verbose_name_plural = 'FAL Classes'

	def __unicode__(self):
		return self.name

class Interview(models.Model):
	interviewer = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, related_name='interviewer', )
	interviewee = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, related_name='interviewee', )
	group = models.ForeignKey(Group)
	date = models.DateTimeField()

	def __unicode__(self):
		return 'Interview of ' + str(interviewee) + ' by ' + str(interviewer)

class Question(models.Model):
	name = models.CharField(max_length=128)
	created_by = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, )
	creation_date = models.DateTimeField()

	def __unicode__(self):
		return self.name

class Interview_Question_Map(models.Model):
	interview = models.ForeignKey(Interview, on_delete=models.CASCADE, )
	question = models.ForeignKey(Question, on_delete=models.CASCADE, )
	
class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, )
	name = models.CharField(max_length=128)
	created_by = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, )
	creation_date = models.DateTimeField()

	def __unicode__(self):
		return self.name

class Video(models.Model):
	interview = models.ForeignKey(Interview, on_delete=models.CASCADE, null=True, blank=True, )
	url = models.CharField(max_length=128)
	tags = models.CharField(max_length=128)
	created_by = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, )
	creation_date = models.DateTimeField()

	def __unicode__(self):
		return 'self.name'

class Question_Video_Map(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, )
	video = models.ForeignKey(Video, on_delete=models.CASCADE, )

class Interview_Question_Video_Map(models.Model):
	interview_question = models.ForeignKey(Question_Video_Map, on_delete=models.CASCADE, )
	video = models.ForeignKey(Video, on_delete=models.CASCADE, )

class Video_Comment(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, )
	my_user = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, related_name='Commenter')
	comment = models.CharField(max_length=128)
	created_by = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, )
	creation_date = models.DateTimeField()

	class Meta:
		verbose_name = 'Video Comment'
		verbose_name_plural = 'Video Comments'

	def __unicode__(self):
		return self.name

class Assignment(models.Model):
	name = models.CharField(max_length=128)
	teacher = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, related_name='Teacher')
	document = models.CharField(max_length=128)
	due_date = models.DateTimeField()
	creation_date = models.DateTimeField()

	def __unicode__(self):
		return self.name

def Assignment_Submission(models.Model):
	name = models.CharField(max_length=128)
	group = models.ForeignKey(Group)

def Submission_Interview_Map(models.Model):
	submission = models.ForeignKey(Assignment_Submission, on_delete=models.CASCADE, )
	interview = models.ForeignKey(Interview, on_delete=models.CASCADE, )
