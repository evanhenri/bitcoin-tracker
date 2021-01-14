from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'refresh-cache': {
        'task': 'bitcoin_tracker.tasks.refresh_cache',
        'schedule': crontab(),  # execute every minute
    },
}
