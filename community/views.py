import random
from unittest import result
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("test")
def calculator(request):
    # data
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')

    operators = request.GET.get('operators')
    
    # calc
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0


    # response

    return render(request, 'calculator.html', {'result': result})

def lotto(request):

    # lotto
    # random.randint(1,45)
    operators = request.GET.get('operators')
    if operators:
        dist= range(1,46)
        result = random.sample(dist,7)
    else:
        result = "로또 번호 추출하기를 눌러주세요!"
    # response
    return render(request, 'lotto.html', {'result': result})