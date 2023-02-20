from django.db import models

# Create your models here.


class Teacher (models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    profile = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    data_join = models.DateField()

    def __str__(self):
        return self.name

