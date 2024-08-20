from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Bootcamp, comment_for_bootcamp

def search_bootcamp_by_name(request, name):
    bootcamp = get_object_or_404(Bootcamp, name=name)
    comments = comment_for_bootcamp.objects.filter(bootcamp=bootcamp)
    comments_list = [comment.text for comment in comments]

    bootcamp_dict = {
        'name': bootcamp.name,
        'start_date': bootcamp.start_date,
        'end_date': bootcamp.end_date,
        'price': bootcamp.price,
        'about_bootcamp': bootcamp.about_bootcamp,
        'capacity': bootcamp.capacity,
        'comments': comments_list,
    }

    return JsonResponse(bootcamp_dict, safe=False)

def search_bootcamp_by_price(request, start, end):
    bootcamps = Bootcamp.objects.filter(price__gt=start, price__lt=end)
    result_list = []

    for bootcamp in bootcamps:
        comments = comment_for_bootcamp.objects.filter(bootcamp=bootcamp)
        comments_list = [comment.text for comment in comments]

        bootcamp_dict = {
            'name': bootcamp.name,
            'start_date': bootcamp.start_date,
            'end_date': bootcamp.end_date,
            'price': bootcamp.price,
            'about_bootcamp': bootcamp.about_bootcamp,
            'capacity': bootcamp.capacity,
            'comments': comments_list,
        }
        result_list.append(bootcamp_dict)

    return JsonResponse(result_list, safe=False)

