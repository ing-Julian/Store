from django.db import models 


class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    price = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
