from django.contrib import admin
from models import * 

modList = [LMS, LMS_Web_Service, School, My_User, Class, Assignment, Question, Answer, Video, Video_Comment, Interview]
admin.site.register(modList)