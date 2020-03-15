import datetime
import celery
import logging
from django.db.models import F

from tochka_test.celery import app
from accounts.models import Account

@app.task
def substract_money_from_hold():
    Account.objects.filter(status='открыт').update(balance=F('balance')-F('hold'), hold=0)
    print('substract_money_from_hold is completed')
