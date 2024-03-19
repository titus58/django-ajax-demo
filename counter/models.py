from django.db import models

# Create your models here.
class Counter(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.name}"
