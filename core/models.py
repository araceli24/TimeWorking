from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Project(models.Model):

    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def time_calculator(self, user):
        timers = self.activityjournal_set.filter(
            user=user).values_list('start', 'end')

        total_time = datetime.timedelta(0)

        for time in timers:
           if time[1] != None:
               diferencia = time[1]-time[0]
               total_time += diferencia

        return total_time
    


    def time_calculators(self, user):
        timers = self.activityjournal_set.filter(
            user=user, project=self).values_list('time_lapse')
        total_time = 0
        for time in timers:
            if time[0] != None:
                total_time += time[0]

        return str(datetime.timedelta(seconds=total_time))

    def __str__(self):
        return self.name


class ActivityJournal(models.Model):
    start = models.DateTimeField(datetime.datetime.now())
    end = models.DateTimeField( null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    time_lapse = models.IntegerField(blank=True, null=True)


    def close_activity(self):
       self.end = timezone.now()
       diff = self.end - self.start
       self.time_lapse = int(diff.total_seconds())
       self.save()


    def __str__(self):
        return '%s %s' % (self.user, self.project)


class Registry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField(datetime.datetime.now())
    end = models.DateTimeField( blank=True)

    def total_worked(self):
        return timezone.now() - self.start

    def check_out(self):
        self.end = timezone.now()
        self.save()

    def __str__(self):
       return 'Usuario: {}, Hora de entrada: {}'.format(self.user, self.start)