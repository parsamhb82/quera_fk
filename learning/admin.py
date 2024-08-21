from learning.models import Class , Bootcamp
from django.contrib.admin import register, ModelAdmin



@register(Class)
class ClassAdmin(ModelAdmin):
    list_display = [
        "name",
        "assingment",
        "lesson"
    ]

@register(Bootcamp)
class BootAdmin(ModelAdmin):
    list_display=[
        "name",
        "start_date",
        "duration",
        "price"
    ]