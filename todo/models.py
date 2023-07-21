from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=250)

    def __str__(self):
        return self.title.__str__()

