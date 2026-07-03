from django.db import models

# Create your models here.
class Register_Master(models.Model):
    Reg_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=40,unique=True)
    Mobile=models.CharField(max_length=12)
    Password=models.CharField(max_length=30)
    Gender =models.CharField(max_length=30)
    DOB=models.DateField()
    Address=models.CharField(max_length=200)
    Role_Name=models.CharField(max_length=20)
    status=models.IntegerField(default=0)
    def __str__(self):
        return self.Name

