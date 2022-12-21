from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'members'
urlpatterns = [
    path('', views.signup_view, name='signup_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('signup2/', views.signup_view2, name='signup_view2'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login,name='login'),
]