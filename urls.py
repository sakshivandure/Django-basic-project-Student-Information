from django.urls import path
from .import views

urlpatterns = [
	   path('',views.home,name='home'),
	   path('register',views.register,name='register'),
       path('insert',views.insert,name='insert'),
	   path('delete',views.delete,name='delete'),
	   path('update',views.update,name='update'),
	   path('view1',views.view1, name='view1'),
	   path('search',views.search, name='search'),
	   path('sort',views.sort, name='sort'),
	
	   

]