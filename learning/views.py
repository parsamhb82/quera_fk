from django.http.response import HttpResponse , JsonResponse
from learning.models import Class , Bootcamp


def class_list(request):
    cls = Class.objects.all()
    cls_list = []
    for item in cls:
        cls_dict = {
            "name":item.name,
            "assigment":item.assingment.name,
            "lesson":item.lesson.subject
        }
        cls_list.append(cls_dict)
    return JsonResponse(cls_list , safe=False)


def bootcamp_list(request):
    btc = Bootcamp.objects.all()
    btc_list = []
    for item in btc:
        btc_dict = {
            "name":item.name,
            "start":item.start_date,
            "duration":item.duration,
            "price":item.price
        }
        btc_list.append(btc_dict)
    return JsonResponse(btc_list , safe=False)

