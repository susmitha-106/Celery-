from django.urls import path
from .views import testView
from .views import testView,send_mail_to_all_users


urlpatterns = [
    path('', testView,name="testView"),
    path('sendmail/', send_mail_to_all_users,name="send_mail_to_all_users"),
    
]