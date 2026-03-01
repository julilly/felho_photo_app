from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('order/name/', views.order_photos_by_name, name='order_by_name'),
    path('order/date/', views.order_photos_by_date, name='order_by_date'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('delete/<int:pk>/', views.delete_photo, name='delete_photo'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='photos/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]