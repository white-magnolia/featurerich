from django.db import models


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null = True, blank = True, upload_to="task_images/")
    def __str__(self):
        return self.title