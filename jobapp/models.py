from django.db import models

# Create your models here.
class Job(models.Model):
    positionName=models.CharField(max_length=100,default='no name')
    company=models.CharField(max_length=50,default='no name')
    salary=models.CharField(max_length=60,default='10000')
    location=models.CharField(max_length=60,default='no name')
    description=models.CharField(max_length=500,default='no name')
    url=models.CharField(max_length=250,default='no name')
    
    def __str__(self) :
        return(f"{self.positionName}")