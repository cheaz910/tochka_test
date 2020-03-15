from django.db import models
import uuid
import re


class NormalizedCharField(models.CharField):
    def get_prep_value(self, value):
        return re.sub(r'\s+', ' ', super(NormalizedCharField, self).get_prep_value(value)).strip()

    def pre_save(self, model_instance, add):
        return re.sub(r'\s+', ' ', super(NormalizedCharField, self).pre_save(model_instance, add)).strip()


class Account(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = NormalizedCharField(max_length=255)
    balance = models.IntegerField(default=0)
    hold = models.IntegerField(default=0)
    status = models.CharField(max_length=64, default='открыт')

    def __str__(self):
        return self.name