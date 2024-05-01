"""
URL configuration for movies_data project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views  # Importing the DRF view classes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/students/', views.Index.as_view(), name='student-list-create'),  # List and create students
    path('api/students/<int:pk>/', views.Detail.as_view(), name='student-detail'),  # Retrieve, update, and delete a specific student
    path('api/students/add/', views.Add.as_view(), name='student-add'),  # Add a new student
    path('api/students/edit/<int:pk>/', views.Edit.as_view(), name='student-edit'),  # Edit an existing student
    path('api/students/delete/<int:pk>/', views.Delete.as_view(), name='student-delete'),  # Delete an existing student
]  # Serving media files during development

