from django.urls import path , re_path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.redirectToLogin),
    re_path('^login/$',login, {'template_name':'mysite/login.html'}),
    re_path('^home/$', views.Home),
    # re_path('^register/$', views.Register),
]
