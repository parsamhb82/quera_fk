from user.models import User
from django.http.response import HttpResponse, JsonResponse

def my_classes(request ,inp):
    usr = User.objects.get(name = inp)
    cls_dict = {
        "name":usr.classes.name,
        "asiignments":usr.classes.assingment.name,
        "lessons":usr.classes.lesson.subject
    }
    return JsonResponse(cls_dict ,safe=False)


def my_boots(request ,inp):
    usr = User.objects.get(name = inp)

    btc_dict = {
        "name":usr.bootcamps.name,
        "start":usr.bootcamps.start_date
    }  
    return JsonResponse(btc_dict ,safe=False)



