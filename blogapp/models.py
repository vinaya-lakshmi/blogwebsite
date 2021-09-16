from django.db import models
import datetime

# Create your models here.
class blog(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    img = models.ImageField(upload_to="images")
    desc = models.TextField()
    date=models.DateField(default=datetime.date.today)

