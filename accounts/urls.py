from django.urls import path
from .views import user_list, search_by_name, search_bootcamp_for_user


urlpatterns = [
    path('accounts/', user_list),
    path("<str:name>/", search_by_name),
    path('bootcamp/<str:name>/',search_bootcamp_for_user ),
]