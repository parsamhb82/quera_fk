from django.urls import path
from bank.views import question_list ,welcome


urlpatterns = [
    path("list/",question_list),
    path("" , welcome)
]