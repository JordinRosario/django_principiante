from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name='signup'),
    path('task/', views.task, name='task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name ='signin'),
    path('task/crear', views.crear_task, name ='crear_task')

]
