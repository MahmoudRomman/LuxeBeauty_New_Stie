from __future__ import absolute_import,unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") # your project name to get the settings file
app = Celery("project") # celery application name

#we are using asia/kolkata time so we are making it False
app.conf.enable_utc=False
app.conf.update(timezone='Africa/Cairo')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


#celery beat settings
app.conf.beat_schedule={

}