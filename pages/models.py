from django.db import models
from django.utils.timezone import now

class Contact(models.Model):
    fullname= models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=60, blank=True)
    message = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.fullname