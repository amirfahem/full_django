from rest_framework import serializers
from .models import Dom, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tag
        fields = ["tag_dom"]

class DomSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    class Meta: 
        model = Dom
        fields = ["type", "price", "image", "title","tag"]