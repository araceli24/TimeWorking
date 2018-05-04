import factory
from .models import Project
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    project_name = factory.Faker('last_name', locale='en_US')
    description = factory.Faker('text')
