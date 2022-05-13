from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.List_create_StudentAPI.as_view()),
    path('studentapi/<int:pk>/', views.Retrive_Update_Delete_StudentAPI.as_view()),
    
    
]
