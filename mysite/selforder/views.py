from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json, requests

# Create your views here.

def categories(request):
    token = '2421054c4b1c00c3e19cd744e3a0437c'
    url = 'http://hardcats.joinposter.com/api/menu.getCategories'

    # http: // hardcats.joinposter.com / api / menu.getCategories?token = 2421054
    # c4b1c00c3e19cd744e3a0437c
    # data = json.loads(requests.get(url)).text
    # new_offers = json.loads(requests.get(url, params={'utoken': clicksmob_api_key, 'uid': 6272}).text)['offer']

    data = json.loads(requests.get(url, params={'token' : token }).text)

    return JsonResponse(data)