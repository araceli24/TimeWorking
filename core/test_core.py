from django.test import TestCase
from core.models import Project, ActivityJournal
from django.contrib.auth.models import User
from django.utils import timezone as tz
import pytz

import datetime as dt
import pytest

@pytest.mark.django_db
def test_calculate_one_activity():
    project = Project.objects.create()
    user = User.objects.create()
    activity_journal = ActivityJournal.objects.create(
        project=project,
        user=user,
        start=tz.datetime(2018, 4, 18, 14, 0, 0, tzinfo=pytz.timezone('Europe/Madrid')),
        end=tz.datetime(2018, 4, 18, 15, 0, 0, tzinfo=pytz.timezone('Europe/Madrid')),
    )
        
    total_time = project.time_calculator(user=user)
    assert(tz.timedelta(hours=1))== total_time


@pytest.mark.django_db
def test_close_activity():
    project = Project.objects.create()
    user = User.objects.create()
    start_date = tz.now()-tz.timedelta(hours=3)
    activity_journal = ActivityJournal.objects.create(
            project=project,
            user=user,
            start=start_date,
    )
    activity_journal.close_activity()
    assert activity_journal.time_lapse == tz.timedelta(hours=3).total_seconds()
