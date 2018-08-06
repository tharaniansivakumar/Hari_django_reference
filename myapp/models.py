from django.db import models

# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=30)
    age=models.IntegerField()
    dish=models.CharField(max_length=30)
    phno=models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table="details"

