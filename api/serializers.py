from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import Project, Registry, ActivityJournal


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=Project
        fields=('user', 'name', 'description')

class RegistrySerializer(serializers.ModelSerializer):

    class Meta:
        model=Registry
        fields=('start', 'end', 'user')

class ActivityJournalSerializer(serializers.ModelSerializer):

    class Meta:
        model=ActivityJournal
        fields=('start', 'end', 'user', 'project', 'time_lapse')
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('username', 'password')