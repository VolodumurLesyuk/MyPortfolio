from django.db import models


class Project(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
