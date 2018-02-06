from django.urls import path , re_path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.redirectToLogin),
    re_path('^login/$',login, {'template_name':'mysite/login.html'}),
    re_path('^home/$', views.Home,name='home'),
    re_path('^register/$', views.Register),
    re_path('^logout/$', views.logOut),
    re_path('^home/profile/(?P<pk>\d+)$', views.Profile),
    re_path('^mybooks/$',views.mybooks,name='mybooks'),
    re_path('^authors/$',views.authors,name='authors'),
    re_path('^favorite/$',views.favorite,name='favorite'),
    re_path('^now/$',views.now,name='now'),
    re_path('^future/$',views.future,name='future'),
]
