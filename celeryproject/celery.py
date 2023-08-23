from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celeryproject.settings")
app = Celery("celeryproject")

#we are using asia/kolkata time so we are making it False
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object("django.conf:settings", namespace = "CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"request: {self.request!r}")

# celery beat settings
app.conf.beat_scheduler={
     'send-mail-everyday-at-14-59':{
        'task':'mailfireapp.tasks.send_mail_func',
        'schedule': crontab(hour=14,minute=59),
        # we can pass arguments here and we can use those in
        # firemailapp/tasks.py send_mail_func function for 
        # that you need one extra argument in your function
        # currently we are not doing that
        # 'args': (1000,)  
    }
    
}