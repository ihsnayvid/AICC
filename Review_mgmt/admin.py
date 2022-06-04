from django.contrib import admin
from . models import review
from django.contrib.admin.options import ModelAdmin
# Register your models here.
class reviewAdmin(ModelAdmin):
	list_display=['email','feedback','Date_Created']
	search_fields=['email','feedback','Date_Created']
	list_filter=['Date_Created']
admin.site.register(review,reviewAdmin)

# Register your models here.
