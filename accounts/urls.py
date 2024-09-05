from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

urlpatterns=[
path('logo/',views.logo_view,name='logo'),
path('logout/',views.logout_view,name='logout'),
path('login/',views.login_view,name='login'),
path('register/',views.register,name='register'),
path('',views.home,name='home'),
#path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
