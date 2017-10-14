from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User)