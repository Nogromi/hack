from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json, requests
import socket


# Create your views here.

def categories(request):
    token = '2421054c4b1c00c3e19cd744e3a0437c'
    url = 'http://hardcats.joinposter.com/api/menu.getCategories'

    # http: // hardcats.joinposter.com / api / menu.getCategories?token = 2421054
    # c4b1c00c3e19cd744e3a0437c
    # data = json.loads(requests.get(url)).text
    # new_offers = json.loads(requests.get(url, params={'utoken': clicksmob_api_key, 'uid': 6272}).text)['offer']

    data = json.loads(requests.get(url, params={'token': token}).text)

    return JsonResponse(data)


def products(request):
    token = '2421054c4b1c00c3e19cd744e3a0437c'
    url = 'http://hardcats.joinposter.com/api/menu.getProducts'

    # category_id = 3
    if request.method == 'GET':
        category_id = request.GET['category_id']
        print(category_id)
        data = json.loads(requests.get(url, params={'token': token, 'category_id': category_id}).text)

        return JsonResponse(data)
    else:
        print("name: ", request, "type: ", request.method)
        category_id = request.POST['category_id']

        data = json.loads(requests.get(url, params={'token': token, 'category_id': category_id}).text)

        return JsonResponse(data)

def tables(request):
    token = '2421054c4b1c00c3e19cd744e3a0437c'
    url = 'http://hardcats.joinposter.com/api/spots.getTableHallTables'

    data = json.loads(requests.get(url, params={'token': token, 'spot_id': 1, 'hall_id': 1, 'without_deleted' : 1 }).text)

    return JsonResponse(data)
