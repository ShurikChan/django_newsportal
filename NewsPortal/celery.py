import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')
 
app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'emails_every_monday': {
        'task': 'notify_every_monday',
        'schedule': 5,
    },
}