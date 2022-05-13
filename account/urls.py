from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('profile/', views.user_profiles, name='aboutuser'),
    path('log_out/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
]
