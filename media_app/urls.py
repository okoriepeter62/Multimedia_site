from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),

    path('edit/<int:id>/', views.edit_media, name='edit'),
    path('delete/<int:id>/', views.delete_media, name='delete'),
]
