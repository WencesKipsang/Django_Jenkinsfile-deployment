from django.urls import path
from cicd import views

urlpatterns = [
    path('heye/', views.home ,name = 'welcome'),
]