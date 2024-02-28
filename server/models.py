from django.db import models
#---------------------------
class Urls(models.Model):
    url = models.CharField(max_length=500)


    def __str__(self):
        return self.url
#---------------------------

