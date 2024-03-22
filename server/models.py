from django.db import models
#---------------------------
class Urls(models.Model):
    applicant_site = models.CharField(max_length=300,default="None",null=True,blank=True)
    url = models.CharField(max_length=500)


    def __str__(self):
        return self.url
#---------------------------

