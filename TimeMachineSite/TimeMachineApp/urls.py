from django.urls import path
from TimeMachineApp import views

app_name = 'TimeMachineApp'

urlpatterns = [
    path('register/', views.register, name='register' ),
    
]