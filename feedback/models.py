from django.db import models

import uuid

from account.models import User

# Create your models here.

class Feedback(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    desc = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='feedbacks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name