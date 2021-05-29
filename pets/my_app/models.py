import uuid

from django.db import models

# Create your models here.
from django.db import models


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    type = models.CharField(max_length=255)
    photos = models.ImageField(upload_to='images/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
