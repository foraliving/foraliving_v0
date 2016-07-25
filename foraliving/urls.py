from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
]
