"""sharm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from amir_app.views import DOMApiView, DomListView,DomCreateView,DomDetailView,DomTypeView,DomTagListView,DomUpdateView, ShoseCreateView,ShoseDetailView,ShoseListView,ShoseUpdateView,ShoseMarkListView

urlpatterns = [
    path("", include("amir_app.urls",namespace ="shose")),
    path("admin/", admin.site.urls),
    path("collections/", DomListView.as_view(),name="list_view"),
    path("collections/<int:pk>/", DomDetailView.as_view(),name="detail_view"),
    path("collnew/", DomCreateView.as_view(),name="craete_view"),
    path("collections/update/<int:pk>/", DomUpdateView.as_view(),name="update_view"),
    path("collections/new", DomTypeView.as_view(),kwargs={"new":None}, name="dom_type_view" ),
    path("collections/modern", DomTagListView.as_view(),kwargs={"modern":None}, name="dom_tag_view" ),
    path("api/dom", DOMApiView.as_view(),name="dom_api_listview")
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)