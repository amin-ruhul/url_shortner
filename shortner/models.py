
from django.db import models

from .util import code_generator ,create_shortner





# Create your models here.

class UrlShortnerManager(models.Manager):

    def all(self,*args,**kwargs):
        qs_main = super(UrlShortnerManager,self).all(*args,**kwargs)
        qs = qs_main.filter(active = True)
        return qs 

    
    def refresh_shortner(self):
        qs = UrlShortner.objects.filter(id__gte=1)
        new_code = 0 
        for q in qs:
            q.shortcode = create_shortner(q)
            q.save()
            new_code += 1
        return "New Code Made: {i} ".format(i = new_code)

class UrlShortner(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15,unique=True,blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = UrlShortnerManager()



    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortner(self)
        super(UrlShortner,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.url)