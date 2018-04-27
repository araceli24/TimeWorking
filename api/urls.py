from django.urls import path, include
from django.conf.urls import url

from rest_framework import routers

from . import views


router=routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet, base_name='projects')
router.register(r'activity-journal', views.ActivityJournalViewSet, base_name='activity-journals')
router.register(r'registry', views.RegistryViewSet, base_name='registry')
router.register(r'user', views.UserViewSet, base_name='users')

urlpatterns = [


    path('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))


]