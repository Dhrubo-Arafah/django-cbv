from django.db import models
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk':self.pk})
