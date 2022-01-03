from django.contrib import admin
from django.urls import path
from .views import signupfunc, loginfunc, mainfunc, logoutfunc, ClanuserCreate, ClanuserDelete, ClanuserUpdate

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('main/', mainfunc, name='main'),
    path('logout/', logoutfunc, name='logout'),
    path('createclanuser/', ClanuserCreate.as_view(), name='createclanuser'),
    path('deleteclanuser/<int:pk>', ClanuserDelete.as_view(), name='deleteclanuser'),
    path('updateclanuser/<int:pk>', ClanuserUpdate.as_view(), name='updateclanuser')
]