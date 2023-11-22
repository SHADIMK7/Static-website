from django.db import models


# Create your models here.
class table1(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class team(models.Model):
    T_name = models.CharField(max_length=250)
    pos = models.CharField(max_length=250)
    des = models.TextField()
    T_img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.T_name
