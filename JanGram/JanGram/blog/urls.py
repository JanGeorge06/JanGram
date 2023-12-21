from django.urls import path
from . import views

urlpatterns = [
    path('',views.feed,name='feed'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile')
]