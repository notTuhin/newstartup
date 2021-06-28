from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.CompanyListView.as_view(), name='companies'),
	path('create/', views.CompanyCreateView.as_view(), name='addcompany'),
	path('post/<int:pk>/', views.CompanyDetailView.as_view(), name ='company-detail'),
	path('post/<int:pk>/edit/', views.CompanyUpdateView.as_view(), name ='company-update'),
	path('post/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name ='company-delete'),


]