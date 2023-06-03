from django.contrib import admin

# Register your models here.

from . models import *

class TestAdmin(admin.ModelAdmin):
    list_display = ['id','field_image','field_json','field_file']

admin.site.register(Test,TestAdmin)