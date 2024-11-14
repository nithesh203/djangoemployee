from django.contrib import admin

from django.urls import path
from app1 import views

app_name="app1"

urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.add,name="add"),
    path('detail/<int:m>/',views.detail,name="detail"),
    path('edit/<int:m>/',views.edit,name="edit"),
    path('delete/<int:m>/',views.delete,name="delete"),

]