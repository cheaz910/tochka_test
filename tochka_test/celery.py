from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tochka_test.settings')

from django.conf import settings

app = Celery('tochka_test')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'run-every-ten-minutes': {
        'task': 'accounts.tasks.substract_money_from_hold',
        'schedule': 600,  # 10 minutes
    },
}
