from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_detail/<int:pk>/', views.post_detail, name='detail'),
    path('update_post/<int:pk>/', views.update_post, name='update'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete'),
]