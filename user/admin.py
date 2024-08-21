from django.contrib.admin import register, ModelAdmin
from user.models import User

@register(User)
class ClassAdmin(ModelAdmin):
    list_display = [
        "name",
        "last_name",
        "email",
        "classes",
        "bootcamps"
    ]