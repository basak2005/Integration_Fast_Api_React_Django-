from django.db import models
from datetime import datetime

class Note(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    note = models.TextField()
    important = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']