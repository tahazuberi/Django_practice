from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.first_prog,name='first_prog')
]