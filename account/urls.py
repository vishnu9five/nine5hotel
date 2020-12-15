from django.urls import path
from . import views

urlpatterns=[
	path('login',views.login, name='login'),
	path('logout',views.logout, name='logout'),
	path('register',views.register, name='register'),
	path('owner_register',views.owner_register, name='owner_register'),
	path('choose',views.choose, name='choose')
]