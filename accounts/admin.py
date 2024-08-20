from django.contrib.admin import register, ModelAdmin
from .models import *
@register(User)
class accounts(ModelAdmin):
    list_display = ['name','last_name']
