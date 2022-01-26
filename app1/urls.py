from django.urls import path
from .views import *
urlpatterns=[
  path('',Home.as_view(),name='home_view'),
  path('detail/<int:pk>',Detail.as_view(),name='detail_view'),
  path('create/',Add.as_view(),name='create_view'),
  path('edit/<int:pk>',Edit.as_view(),name='edit_view'),
  path('delete/<int:pk>',Delete.as_view(),name='delete_view'),
  path('category/',AddCat.as_view(),name='addcat_view'),
  path('catdetail/<str:var>',Catdetail,name='catdetail_view'),
  path('catlist/',Catlist,name='catlist_view'),
]