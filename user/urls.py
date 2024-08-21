from django.urls import path
from user.views import my_boots ,my_classes


urlpatterns = [
    path("my_boot/<str:inp>",my_boots),
    path("my_class/<str:inp>" , my_classes)
]