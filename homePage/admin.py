from django.contrib import admin
from .models import Record, RecordImage
# Register your models here.


class RecordImageInline(admin.TabularInline):
    model = RecordImage
    extra = 6

class RecordAdmin(admin.ModelAdmin):
    list_display = ('vase_num', 'collection', 'technique', 'scholor_name')
    inlines = [ RecordImageInline, ]

admin.site.register(Record, RecordAdmin)