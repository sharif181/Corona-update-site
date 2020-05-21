from django.shortcuts import render
from django.http import HttpResponse
from .models import info,worldInfo
from bs4 import BeautifulSoup as bs
import requests as r


response = r.get("https://www.worldometers.info/coronavirus/")

raw_data = response.content
soup = bs(raw_data,'lxml')

def home(request):

    # result = info.objects.get(id=1)
    labels = ['Infected', 'Died', 'Survive']
    # data=[result.number_of_infected,result.number_of_death,result.number_of_survive]
    ban = []
    for tr in soup.find_all('tr'):
      if "Bangladesh" in tr.text:
        ban.append(tr.text)

    x = ban[0].split("\n")
    data = [int (x[3].replace(',','')),int(x[5].replace(',','')),int(x[7].replace(',',''))]

    return render(request,'index.html',
                  {'labels':labels,
                    'data': data
                   })


def worldview(request):
    # result = worldInfo.objects.get(id=1)
    labels = ['Infected', 'Died', 'Survive']
    # data = [result.number_of_infected, result.number_of_death, result.number_of_survive]

    spans = []
    for span in soup.find_all('div',{"class":"maincounter-number"}):

      s = span.find('span')
      spans.append(s.text)

    data = []
    for x in spans:
      data.append(int(x.replace(',' , '')))
    return render(request, 'index.html',
                  {'labels': labels,
                   'data': data
                   })
