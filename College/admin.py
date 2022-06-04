from django.contrib import admin
from .models import clg,MyModel
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.options import ModelAdmin
# Register your models here.

@admin.register(clg)
class collegeAdmin(ImportExportModelAdmin):
	pass

admin.site.register(MyModel)



