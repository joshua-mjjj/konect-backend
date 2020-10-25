from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview_servers, name="api-overview"),
	path('dataset/', views.dataset_view, name="dataset"),
	path('motors_SPs_list/', views.MotorsList, name="dataset"),
	path('motors_detail/<str:pk>/', views.MotorsDetail, name="dataset"),
	path('motors_create/', views.MotorsCreate, name="dataset"),
	path('motors_update/<str:pk>/', views.MotorsUpdate, name="dataset"),
	path('motors_delete/<str:pk>/', views.MotorsDelete, name="dataset"),
]