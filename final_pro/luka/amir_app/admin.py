from django.contrib import admin
from .models import Dom, Variation, Tag, Shose, Mark

admin.site.register(Shose)
admin.site.register(Mark)

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1

class DomAdmin(admin.ModelAdmin):
    inlines = [VariationInline]
    list_display = ["__str__"]
    
    class Meta:
        model = Dom

admin.site.register(Dom,DomAdmin)
admin.site.register(Tag)
