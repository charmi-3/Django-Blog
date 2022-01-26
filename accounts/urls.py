from django.urls import path
from .views import *
urlpatterns =[
    path('signup/',Register.as_view(),name='register_view'),
]