from django.db import models

# Create your models here.

# TASK: 

# one model = one table in DB 
class Student(models.Model):
    # id column will be auto created by Django, no need to create again
    # variables = column name 
    
    # CharField = varchar, use to store string
    # if chars count > max_length, record will not be created in database
    # by default, the column is required, error will occur if left blank
    # to change required -> optional, add 'null' & 'blank' to TRUE
    name = models.CharField(max_length=10, null=True, blank=True)
    