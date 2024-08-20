from django.urls import path
from .views import search_bootcamp_by_name, search_bootcamp_by_price

urlpatterns = [
    path('<str:name>', search_bootcamp_by_name),
    path('<int:start>/<int:end>/', search_bootcamp_by_price),]