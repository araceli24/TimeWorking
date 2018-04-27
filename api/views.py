from rest_framework import viewsets
from .serializers import ProjectSerializer, ActivityJournalSerializer, RegistrySerializer, UserSerializer
from core.models import Project, Registry, ActivityJournal
from django.contrib.auth.models import User
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    serializer_class=UserSerializer
    queryset=User.objects.all()
    

class ProjectViewSet(viewsets.ModelViewSet):

    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
   

class RegistryViewSet(viewsets.ModelViewSet):

    queryset=Registry.objects.all()
    serializer_class=RegistrySerializer


class ActivityJournalViewSet(viewsets.ModelViewSet):

    queryset=ActivityJournal.objects.all()
    serializer_class=ActivityJournalSerializer