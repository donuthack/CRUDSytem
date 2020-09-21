from django.db import models 


class Customer(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    lastname = models.CharField(max_length=70, blank=False, default='')
    age = models.IntegerField(blank=False, default=1)
    address = models.CharField(max_length=70, blank=False, default='')
    copyright = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return self.name




