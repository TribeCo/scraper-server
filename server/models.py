from django.db import models
#---------------------------
class Urls(models.Model):
    url = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.url[:20]
#---------------------------

