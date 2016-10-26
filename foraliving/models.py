# Add documentation link
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models
from datetime import datetime    
# from mptt.models import MPTTModel, TreeForeignKey

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
		return str(self.user)

class Skill(models.Model):
	name = models.CharField(max_length=25)

class Interest(models.Model):
	name = models.CharField(max_length=25)

class Volunteer_User_Add_Ons(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=12, )
	canGetText = models.BooleanField(default=True)
	workTitle = models.CharField(max_length=25)
	isBusinessOwner = models.BooleanField(default=True)
	workIndustry = models.CharField(max_length=25)
	yearsInIndustry = models.IntegerField()
	linkedinProfile = models.CharField(max_length=128, null=True, blank=True, )
	hsGradChoices = (
		(1, '1-4'),
		(2, '5-10'),
		(3, '11 or more'),
		(4, 'Have not graduated'),)
	yearsSinceHSGraduation = models.IntegerField(choices=hsGradChoices)
	collegeLevelChoice = (
		(1, "associate"),
		(2, "bachelor's"),
		(3, "master's"),
		(4, "doctoral"),
		(5, "none"),)
	collegeLevel = models.IntegerField(choices=hsGradChoices)
	collegeMajor = models.CharField(max_length=128, null=True, blank=True, )
	# skills = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
	skills = models.ForeignKey(Skill, null=True, blank=True, )
	# interests = TreeForeignKey('interest-self', null=True, blank=True, related_name='interest-children', db_index=True)
	interests = models.ForeignKey(Interest, null=True, blank=True, )

	# User_Skill_Map
	# User_Interest_Map

	class Meta:
		verbose_name = 'Volunteer add-ons'
		verbose_name_plural = 'Volunteer add-ons'

	def __unicode__(self):
		return "Volunteer: " + str(self.user)
		# return "Volunteer: " 

class User_Group_Role_Map(models.Model):
	group = models.ForeignKey(Group) 
	user = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE)
	role = models.CharField(max_length=128)

	class Meta:
		verbose_name = 'Role'
		verbose_name_plural = 'Roles'

	def __unicode__(self):
		return str(self.group) + ': ' + str(self.user) + '-' + str(self.role)

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
		return str(self.school) + ':' + str(self.teacher)

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
		return str(self.created_by) + ':' + str(self.name)

class Interview_Question_Map(models.Model):
	interview = models.ForeignKey(Interview, on_delete=models.CASCADE, )
	question = models.ForeignKey(Question, on_delete=models.CASCADE, )

	class Meta:
		verbose_name = 'Interview Question'
		verbose_name_plural = 'Interview Questions'

	def __unicode__(self):
		return str(self.question) + ' (' + str(interview) + ')'
	
class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, )
	result = models.CharField(max_length=128)
	created_by = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, )
	creation_date = models.DateTimeField()

	def __unicode__(self):
		return str(self.question)

class Video(models.Model):
	# interview = models.ForeignKey(Interview, on_delete=models.CASCADE, null=True, blank=True, )
	name = models.CharField(max_length=128)
	url = models.CharField(max_length=128)
	tags = models.CharField(max_length=128, null=True, blank=True, )
	created_by = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, )
	creation_date = models.DateTimeField(default=datetime.now, blank=True)

	def __unicode__(self):
		return str(self.name) + ' (' + str(self.creation_date) + ')'

class Question_Video_Map(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, )
	video = models.ForeignKey(Video, on_delete=models.CASCADE, )

	class Meta:
		verbose_name = 'Video Question'
		verbose_name_plural = 'Video Questions'

	def __unicode__(self):
		return str(self.question) + ':' + str(self.video)

class Interview_Question_Video_Map(models.Model):
	interview_question = models.ForeignKey(Question_Video_Map, on_delete=models.CASCADE, )
	video = models.ForeignKey(Video, on_delete=models.CASCADE, )

	class Meta:
		verbose_name = 'Interview Question Video'
		verbose_name_plural = 'Interview Video Questions'

	def __unicode__(self):
		return str(self.interview_question) + '-' + str(self.video)

class Video_Comment(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, )
	comment = models.CharField(max_length=128)
	created_by = models.ForeignKey(User_Add_Ons, on_delete=models.CASCADE, )
	creation_date = models.DateTimeField()

	class Meta:
		verbose_name = 'Video Comment'
		verbose_name_plural = 'Video Comments'

	def __unicode__(self):
		return str(self.video) + ' (' + str(created_by) + ', ' + str(creation_date) + ')'

class Assignment(models.Model):
	title = models.CharField(max_length=128)
	falClass = models.ForeignKey(Class, on_delete=models.CASCADE)
	document = models.CharField(max_length=128)
	due_date = models.DateTimeField()
	creation_date = models.DateTimeField()

	def __unicode__(self):
		return str(self.title) + ' (' + str(falClass) + ')'

class Assignment_Submission(models.Model):
	name = models.CharField(max_length=128)
	group = models.ForeignKey(Group)

	class Meta:
		verbose_name = 'Submission'
		verbose_name_plural = 'Submissions'

	def __unicode__(self):
		return str(self.group) + ':' + str(self.name)

class Submission_Interview_Map(models.Model):
	submission = models.ForeignKey(Assignment_Submission, on_delete=models.CASCADE, )
	interview = models.ForeignKey(Interview, on_delete=models.CASCADE, )

	class Meta:
		verbose_name = 'Interview Submission'
		verbose_name_plural = 'Interview Submissions'

	def __unicode__(self):
		return str(self.submission) + ':' + str(self.interview)