from django.urls import path
from student.views import *
urlpatterns=[
path('search',search,name="search"),
path('Addstud',Addstud,name="Addstud"),
path('Dispstd',Dispstd,name="Dispstd"),
path('showsub',showsub,name="showsub"),
]
