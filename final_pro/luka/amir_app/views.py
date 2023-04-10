from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from rest_framework import generics
from .serializers import DomSerializer
from .models import Dom, Variation, Tag, Shose, Mark

class DOMApiView(generics.ListAPIView):
    queryset = Dom.objects.all()
    serializer_class = DomSerializer

class DomListView(ListView):
    model = Dom
    template_name = "amir_app/allproducts.html"
    def get_context_data(self,**kwargs):
        context = super(DomListView, self).get_context_data(**kwargs)
        var_otherproducts =  Dom.objects.all()
        var_shoes  = Shose.objects.all()
        context["shoes"] = var_shoes
        context["otherproducts"] = var_otherproducts
        return context

class DomTypeView(ListView):
    model = Dom
    template_name = "amir_app/filter.html"
    def get_context_data(self,**kwargs):
        context = super(DomTypeView, self).get_context_data(**kwargs)
        var_name = self.request.GET["new"]
        context['key'] = "First Result {} ".format(var_name)
        another_var = Dom.objects.filter(type = var_name)
        context["another_var"] = another_var
        return context


class DomTagListView(ListView):     

    model = Dom
    template_name = "amir_app/filter_tag.html"

    def get_context_data(self, **kwargs):
        context = super(DomTagListView,self).get_context_data(**kwargs)
        var_name_two = self.request.GET["modern"]
        context["key"] = "Second Result {}".format(var_name_two)
        var_main= Dom.objects.filter(tag__tag_dom= var_name_two)
        context["second_filter"] = var_main
        return context
      
class DomDetailView(DetailView):
    model = Dom

class DomCreateView(CreateView):
    model = Dom
    fields = ["type", "title","price",  "image"]

class DomUpdateView(UpdateView):
    model = Dom
    fields = ["type","title", "price", "image"]



class ShoseListView(ListView):
    
    model = Shose
class ShoseMarkListView(ListView):
    model = Shose
    template_name ="amir_app/filter_mark.html"
    def get_context_data(self, **kwargs):
        context = super(ShoseMarkListView , self).get_context_data(**kwargs)
        filter_mark =self.request.GET["old"]
        print(filter_mark)
        context["key"] = "result of old collection {}".formar(filter_mark)
        old_filter = Shose.objects.filter(mark_mark__shose=filter_mark)
        context["fourth_filter"] = old_filter
        return context


class ShoseDetailView(DetailView):
     model = Shose

class ShoseCreateView(CreateView):
    model = Shose
    fields = ["model", "brand_shose", "size_shose", "image"]

class ShoseUpdateView(UpdateView):
    model = Shose
    fields = ["model", "brand_shose", "size_shose", "image"]
