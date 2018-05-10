from django.contrib import admin
from .models import Registry
from .models import Project
from .models import ActivityJournal

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )


class RegistryAdmin(admin.ModelAdmin):
    list_filter = ('start',)
    list_display = ('user', 'start', 'end')


class ActivityJournalAdmin(admin.ModelAdmin):
    list_filter = ('start', 'end', 'project',)
    list_display = ('user', 'project', 'start', 'end')

# Register your models here.
admin.site.register(Registry)
admin.site.register(Project)
admin.site.register(ActivityJournal)
