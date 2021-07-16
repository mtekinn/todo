from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('updateTask/<str:id>/', views.updateTask, name="updateTask"),
    path('delete/<str:id>/', views.deleteTask, name="delete"),
]