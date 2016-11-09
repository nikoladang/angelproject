from django.contrib import admin
from shortener.models import Urls
from import_export import resources
 
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','original_url','views_total','create_date')
    ordering = ('-create_date',)
 
admin.site.register(Urls, UrlsAdmin) # Register the Urls model with UrlsAdmin options


# class UrlsResource(resources.ModelResource):
#
#     class Meta:
#         model = Urls