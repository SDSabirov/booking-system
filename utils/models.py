from django.db import models


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is created
    modified = models.DateTimeField(auto_now=True)    # Automatically updated every time the object is saved

    class Meta:
        abstract = True 