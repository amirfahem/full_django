
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from amir_app.views import DomListView,DomCreateView,DomDetailView,DomTypeView,DomTagListView,DomUpdateView, ShoseCreateView,ShoseDetailView,ShoseListView,ShoseUpdateView,ShoseMarkListView

app_name= "shose"
urlpatterns = [
    path("shoses/", ShoseListView.as_view(),name="shose_list_view"),
    path("shoses/<int:pk>/", ShoseDetailView.as_view(),name="shose_detail_view"),
    path("shosenew/", ShoseCreateView.as_view(),name="shose_craete_view"),
    path("shoses/update/<int:pk>/", ShoseUpdateView.as_view(),name="shose_update_view"),
    path("shoses/filter/", ShoseMarkListView.as_view(),kwargs={"old":None}, name="shose_filter_view" ),
]
