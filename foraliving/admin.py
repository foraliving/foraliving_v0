from django.contrib import admin
from .models import * 

# This should do for the time being. We'll add customization as needed 
modList = [LMS, LMS_Web_Service, School, My_User, Class, Assignment, Question, Answer, Video, Video_Comment, Interview]
admin.site.register(modList)