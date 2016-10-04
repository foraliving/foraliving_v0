from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib import admin
from . import views
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^$", views.index, name="home"),
    url(r"^setup/", views.interviewSetup, name="setup"),
    url(r"^record/", views.record, name="record"),
    url(r"^theme/", views.sitetheme, name='theme'),
    url(r"^volunteer-signup/", views.volunteerSignup, name='vSignup'),
    # url(r'^$', views.home, name='home'),
]
