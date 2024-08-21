from django.urls import path
from learning.views import class_list , bootcamp_list

urlpatterns = [
    path("bootcamp/",bootcamp_list),
    path("class/" , class_list)
]