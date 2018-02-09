from django.urls import path , re_path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.redirectToLogin),
    re_path('^login/$',login, {'template_name':'mysite/login.html'}),
    re_path('^home/$', views.Home,name='home'),
    re_path('^register/$', views.Register),
    re_path('^logout/$', views.logOut),
    re_path('^home/profile/(?P<pk>\d+)$', views.profile),
    re_path('^mybooks/$',views.myBooks,name='mybooks'),
    re_path('^authors/$',views.authors,name='authors'),
    re_path('^favorite/$',views.favorite,name='favorite'),
    re_path('^now/$',views.now,name='now'),
    re_path('^future/$',views.future,name='future'),
    re_path('^search/$',views.search,name='search'),
    path('mybooks/remove/<int:remove_id>', views.remove),
    path('mybooks/author/<int:author_id>', views.showAuthor, name='author'),
    path('mybooks/book/<int:book_id>', views.showBook, name='book'),
    path('mybooks/rate/', views.rate, name='rate_no'),
    path('mybooks/browse/<int:catno>', views.browse, name='browse'),
    path('mybooks/addbook/<int:add_id>/<slug:state>', views.addBook, name='add'),
    path('mybooks/review/', views.review, name='review'),
]
