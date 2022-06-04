from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
# Register your models here.
from .models import Post,comment
admin.site.register(Post)

admin.site.site_header="AICC Admin"
class commentAdmin(ModelAdmin):
	list_display=['Message','Created_On']
	search_fields=['Created_On']
	list_filter=['Created_On']
	actions=['approve_comments']

	def approve_comments(self,request,queryset):
		queryset.update(active=True)
admin.site.register(comment,commentAdmin)










