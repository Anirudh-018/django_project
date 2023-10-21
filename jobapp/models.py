from django.db import models

# Create your models here.
class Job(models.Model):
    jobName=models.CharField(max_length=50)
    salary=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    description=models.CharField(max_length=500)