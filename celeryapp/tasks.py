from celery import shared_task

@shared_task(bind=True)
def fun(self):
    #opeerations
    print("you are in fun function")
    return "done"