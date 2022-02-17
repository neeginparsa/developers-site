from django.urls import path
from . import views

urlpatterns =[
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),

    path('', views.Profiles, name='profiles'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),

]