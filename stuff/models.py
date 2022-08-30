from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Stuff(models.Model):
    maker = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    explanation = models.TextField()
    time_stamp_creation = models.DateTimeField(auto_now_add=True)
    time_stamp_updation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
