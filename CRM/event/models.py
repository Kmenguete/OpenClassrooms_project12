from django.conf import settings
from django.db import models
from client.models import Client

from contract.models import Contract


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_status = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()
