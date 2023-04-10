
from django.db import models
from django.urls import reverse

class Dom(models.Model):
    type = models.CharField(max_length=100, blank=True, unique=True)
    title = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(blank=True)
    tag = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return "{}, {}" .format(self.type, self.title)
     
    def get_absolute_url(self):
        return reverse ("detail_view", kwargs={"pk":self.id})

class Variation(models.Model):
    dom = models.ForeignKey(Dom, on_delete=models.CASCADE)
    size   =  models.CharField(max_length=40, blank=True)
    color  =  models.CharField(max_length=40, blank=True)
    brand  =  models.CharField(max_length=40, blank=True)
   

class Tag(models.Model):
    tag_dom = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_dom
     

class Shose(models.Model):
    model = models.CharField(max_length=100, blank=True,unique=True)
    brand_shose = models.CharField(max_length=200, blank=True)
    size_shose   =  models.CharField(max_length=200, blank=True)
    mark = models.ManyToManyField("Mark",blank=True)
    image = models.ImageField(blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return "{}, {}" .format(self.model, self.size_shose)
     
    def get_absolute_url(self):
        return reverse ("shose:shose_detail_view", kwargs={"pk":self.id})


class Mark(models.Model):
    mark_shose = models.CharField(max_length=100)
    
    def __str__(self):
        return self.mark_shose


