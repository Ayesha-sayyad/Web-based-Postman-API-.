from django.db import models

class SumRequest(models.Model):
    numbers = models.TextField()
    result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
