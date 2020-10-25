from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview_clients, name="api-users-overview"),
	path('dataset/', views.dataset_users_view),
	path('users_list/', views.UsersList),
	path('user_detail/<str:pk>/', views.UsersDetail),
	path('user_create/', views.UsersCreate),
	
]