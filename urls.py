from django.urls import path
from . import views

urlpatterns = [
    path('api/stream/', views.StreamView.as_view(), name='stream'),
    path('api/record/', views.RecordView.as_view(), name='record'),
    path('api/user/', views.UserView.as_view(), name='user'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/register/', views.RegisterView.as_view(), name='register'),
]