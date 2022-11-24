from django.db import models


class Article(models.Model):

    name=models.CharField(max_length=50,blank=False,default=None)
    section=models.CharField(max_length=20,blank=False, default=None)
    description=models.CharField(max_length=100,blank=False,default=None)
    unit_price = models.DecimalField('Precio Unitario', max_digits=10, decimal_places=2, default=0)
   
    

    def __str__(self):
        return self.name


