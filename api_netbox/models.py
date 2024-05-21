# models.py
from django.db import models

class Netbox(models.Model):
    hostname = models.CharField(max_length=200)
    username = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    pod_count = models.IntegerField(null=True)
    pods = models.JSONField(null=True)


