from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import User

def user_list(request):
    user_accounts = User.objects.all()
    user_list = [
        {
            'name': user.name,
            'last_name': user.last_name,
            'email': user.email,
            'city': user.city,
            'kod_meli': user.kod_meli,
            'phone_number': user.phone_number,
            'date_of_birth': user.date_of_birth,
            'gender': user.gender,
            'about_user': user.about_user,
        }
        for user in user_accounts
    ]
    return JsonResponse(user_list, safe=False)

def search_by_name(request, name):
    user_list = User.objects.filter(name=name)
    if user_list.exists():
        users = [
            {
                'name': user.name,
                'last_name': user.last_name,
                'email': user.email,
                'city': user.city,
                'kod_meli': user.kod_meli,
                'phone_number': user.phone_number,
                'date_of_birth': user.date_of_birth,
                'gender': user.gender,
                'about_user': user.about_user,
            }
            for user in user_list
        ]
        return JsonResponse(users, safe=False)
    else:
        return HttpResponse("Nothing found", status=404)

def search_bootcamp_for_user(request, name):
    user = get_object_or_404(User, name=name)
    bootcamp_list = [bootcamp.name for bootcamp in user.bootcamp.all()]
    user_bootcamp = {
        'name': f"{user.name} {user.last_name}",
        'bootcamp': bootcamp_list,
    }
    return JsonResponse(user_bootcamp)
     