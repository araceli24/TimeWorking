from django.contrib import admin
from .models import Registry
from .models import Project
from .models import ActivityJournal

# Register your models here.
admin.site.register(Registry)
admin.site.register(Project)
admin.site.register(ActivityJournal)
