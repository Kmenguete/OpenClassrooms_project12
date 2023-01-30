from django.conf import settings
from django.db import models

from client.models import Client


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, blank=True)
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Contract N°" + str(self.pk) + " " + str(self.amount) + "€"
