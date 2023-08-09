from django.db import models

#gender=(('Male','Male'),('Female','Female'),('Trans','Trans'),('Prefer not to say','Prefer not to say'))

class content(models.Model):
    
    name=models.CharField(max_length=200,blank=True,default=" ")
    #DOB=models.DateField(blank=True,default=" ")
    #Gender=models.CharField(choices=gender,max_length=30,blank=True,default=" ")
    #Contact_no=models.PositiveIntegerField(blank=True,default=" ")
    #Email=models.EmailField(max_length=100 ,blank=True,default=" ")
    Image=models.ImageField(upload_to="Imagecontant",blank=True,default='  ')
    video=models.FileField(upload_to="DocsContant",blank=True,default=" ")
    Article=models.TextField(max_length=5000,blank=True,default='')

    