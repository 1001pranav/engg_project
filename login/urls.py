from django.urls import path
from login.views import *
urlpatterns=[
path('',login,name='login'),
path('Home',Home,name='Home')
]
