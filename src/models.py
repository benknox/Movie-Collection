import uuid
from django.db import models

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, blank=False)
    duration = models.IntegerField(blank=True, help_text="duration in seconds", default=0)

    class Meta:
        ordering = ['name']