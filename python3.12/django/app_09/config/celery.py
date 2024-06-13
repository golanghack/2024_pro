import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# create celery
app = Celery('config')

# load settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto detect a tasks files
app.autodiscover_tasks()