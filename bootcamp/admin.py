from django.contrib.admin import register, ModelAdmin, TabularInline
from .models import *

class comment(TabularInline):
    model = comment_for_bootcamp
    extra = 0




@register(Bootcamp)
class bootcmap(ModelAdmin):
    list_display =['name', 'price']
    search_fields = ['name']
    inlines = [comment]