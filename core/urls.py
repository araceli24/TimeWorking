#from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path
from . import views
from core.views import ProjectDetail


urlpatterns = [
    url(r'^$', views.project_list, name='project_list'),
    #path('', login_required(views.ProjectListView.as_view()), name='projects_list'),
    #url(r'^project/(?P<pk>\d+)/$', views.project_detail, name='project_detail'),
    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='project_detail'),
    url(r'^project/new/$', views.project_new, name='project_new'),
    url(r'^project/(?P<pk>\d+)/edit/$', views.project_edit, name='project_edit'),
    url(r'^project/(?P<pk>\d+)/delete/$', views.project_delete, name='project_delete'),
    url(r'^project/(?P<pk>\d+)/start/$', views.project_start, name='project_start'),
    url(r'^project/(?P<pk>\d+)/stop/$', views.project_stop, name='project_stop'),
]

