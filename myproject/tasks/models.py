from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True) 
    due_date = models.DateField(blank=True, null=True)  # 期日

    def __str__(self):
        return self.title


# Create your models here.
