from django.db import models


class Task(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
