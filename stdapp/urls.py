from django.contrib import admin
from django.urls import path 
from stdapp import views

urlpatterns = [
    path('', views.person, name='index'),
    path('save/', views.save, name='save'),
    path('edit/', views.edit, name='edit'),
    path('student/', views.std, name='student'),
    path('person/', views.person, name='person'),
    path('form_view/', views.form_view, name='form_view'),
    path('delete/<person_id>' ,views.delete,name='delete'),
    path('edit/<int:person_id>' ,views.edit,name='edit'),
    # ex: /polls/
]