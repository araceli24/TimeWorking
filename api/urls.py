from django.urls import path, re_path, include
from django.conf.urls import url

from rest_framework import routers

from api import views
from . import views

router=routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'activity-journals', views.ActivityJournalViewSet)
router.register(r'registrys', views.RegistryViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include((router.urls, 'api'), namespace='api')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

from rest_framework.authtoken import views
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]