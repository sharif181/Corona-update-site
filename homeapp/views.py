from django.shortcuts import render
from django.http import HttpResponse
from .models import info,worldInfo

def home(request):

    result = info.objects.get(id=1)
    labels = ['Infected', 'Died', 'Survive']
    data=[result.number_of_infected,result.number_of_death,result.number_of_survive]


    return render(request,'index.html',
                  {'labels':labels,
                    'data': data
                   })


def worldview(request):
    result = worldInfo.objects.get(id=1)
    labels = ['Infected', 'Died', 'Survive']
    data = [result.number_of_infected, result.number_of_death, result.number_of_survive]

    return render(request, 'index.html',
                  {'labels': labels,
                   'data': data
                   })