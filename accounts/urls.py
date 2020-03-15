from django.urls import path

from .views import *


app_name = "accounts"

urlpatterns = [
    path('ping/', api_ping),
    path('add/', api_add),
    path('substract/', api_substract),
    path('status/', api_status),
]