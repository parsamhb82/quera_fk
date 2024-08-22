from django.http.response import HttpResponse , JsonResponse
from bank.models import Question

def question_list(request):
    questions = Question.objects.all()
    lst = []
    for item in questions:
        dic = {
            "soal":item.form,
            "level":item.level,
            "attemps":f"{item.given_answers}/{item.correct_answers}"
        }
        lst.append(dic)
    return JsonResponse(lst , safe=False)

def welcome(request):
    return HttpResponse("welcome to question bank")