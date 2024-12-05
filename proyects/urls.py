""" from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls """

from django.urls import path, include
from . import views
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('', views.list_projects, name='list_projects'),
    path('list/', views.list_projects, name='list_projects'),
    path('create/', views.create_project, name='create_project'),
    path('update/<int:id>/', views.update_project, name='update_project'),
    path('delete/<int:id>/', views.delete_project, name='delete_project'),
    path('api/', include(router.urls)),
]
