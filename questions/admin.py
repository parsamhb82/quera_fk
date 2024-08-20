from django.contrib.admin import register, ModelAdmin
from .models import Author, Question

@register(Author)
class author(ModelAdmin):
    list_display = ['name']

@register(Question)
class Question(ModelAdmin):
    list_display = ['title', 'difficulty_level']
    search_fields = ['title', 'difficulty_level']