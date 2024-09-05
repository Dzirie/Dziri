from django.urls import path
from . import views

app_name = 'picture'

urlpatterns=[
path('browse/',views.browse,name='browse'),
path('photos/',views.photos_view,name='photos'),
path('<int:pk>/',views.detail,name='detail'),
path('<int:pk>/delete/',views.delete,name='delete'),
path('<int:pk>/edit/',views.edit,name='edit'),
path('new/',views.new,name='new'),
]
