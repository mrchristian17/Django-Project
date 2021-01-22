from django.urls import path
from .views import (
	ProjectListView, 
	ProjectDetailView, 
	ProjectCreateView,
	ProjectUpdateView,
	ProjectDeleteView
)
from . import views
from users import views as user_views

urlpatterns = [
    path('', ProjectListView.as_view(), name='portfolio_home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name='portfolio_about'),
]