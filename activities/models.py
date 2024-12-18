from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    distance = models.FloatField()  # in kilometers
    duration = models.CharField(max_length=32,null=False,default='00:00')  # in hours:minutes:seconds
    date = models.CharField(max_length=100, null=True, blank=True)  # date as string
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=32,null=False,default='run')
    photos = models.CharField(max_length=255, null=True, blank=True)  # store file path as string
    speed = models.FloatField(null=True, blank=True)  # in km/h (calculated later if needed)
    notes = models.TextField(null=True, blank=True)  # for storing notes
    steps = models.IntegerField(null=True, blank=True)  # number of steps

    def __str__(self):
        return f'{self.name} on {self.date}'
