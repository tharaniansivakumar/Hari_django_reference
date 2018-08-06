from django.db import models


class Workout(models.Model):
    name = models.CharField(max_length=30)
    age=models.IntegerField()
    dish=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class File(models.Model):
    path=models.CharField(max_length=1000)





class Products(models.Model):
    prod_name=models.CharField(max_length=30)

class Phone(models.Model):
    ph_brand=models.CharField(max_length=30)
    ph_name=models.CharField(max_length=30)
    ph_price = models.FloatField()
    ph_img=models.CharField(max_length=30)
    ph_ram=models.CharField(max_length=30)
    ph_rom=models.CharField(max_length=30)
    ph_display=models.CharField(max_length=30)
    ph_battery=models.CharField(max_length=30)

class Lap(models.Model):
    lp_brand = models.CharField(max_length=30)
    lp_name=models.CharField(max_length=30)
    lp_price = models.FloatField()
    lp_img=models.CharField(max_length=30)
    lp_ram=models.CharField(max_length=30)
    lp_rom=models.CharField(max_length=30)
    lp_display=models.CharField(max_length=30)
    lp_battery=models.CharField(max_length=30)


class dateSample(models.Model):
    order_id=models.CharField(max_length=30)
    cancel_date=models.DateTimeField(null=True,blank=True)



class userDetails(models.Model):
    username=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=100)
    token=models.CharField(max_length=200,default=None)

class autoid(models.Model):
    id=models.AutoField(primary_key=100)




class parent(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

class child(models.Model):
    child_id=models.IntegerField(primary_key=True)
    value=models.IntegerField()
    info=models.OneToOneField(parent)


class manyparent(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50,db_column="parent_name")
    class Meta:
        indexes=[
        name=models.Index(fields=['name'],name="parental_name"),
        ]
class manychild(models.Model):
    child_id=models.IntegerField(primary_key=True)
    value=models.IntegerField()
    info=models.ForeignKey(manyparent,db_column="parent_name")

class csvData(models.Model):
    rollno=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=1)
