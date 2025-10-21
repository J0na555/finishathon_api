from django.urls import path
from .views import ProjectListCreateView, UsersProjectList

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='projects-list-create'),
    path('user/', UsersProjectList.as_view(), name='projects-user-list'),
]
