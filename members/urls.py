from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),    
    path('courts/', views.court_list, name='court-list'),  # URL for the courts list
    path('courts/<int:id>/', views.court_detail, name='court-detail'),  # URL for a court's details
]