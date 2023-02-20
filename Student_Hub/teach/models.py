from django.db import models


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='videos/%y/%m/%d')
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
