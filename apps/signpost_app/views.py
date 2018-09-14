import random
import string

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
def index(request):
    return HttpResponse(generate_unique_id())



@csrf_exempt
def create_Thunt(request):
    try:
        first_node = ClueNode.objects.create(
            title = request.POST['title'],
            text = request.POST['text'],
            latitude = request.POST['latitude'],
            longitude = request.POST['longitude'],
            unique_id =  generate_unique_id()
        )
        TreasureHunt.objects.create(
            first_node = first_node
        )
    except:
        return HttpResponse("ERROR")
    return HttpResponse("SUCCESS")

@csrf_exempt
def create_node(request):
    try: 
        prev_node = ClueNode.objects.get(unique_id=request.POST['unique_id'])
        if prev_node.next_node == None:
            ClueNode.objects.create(
                title = request.POST['title'],
                text = request.POST['text'],
                latitude = request.POST['latitude'],
                longitude = request.POST['longitude'],
                prev_node = prev_node,
                unique_id =  generate_unique_id()
            )
    except:
        return HttpResponse("ERROR")
    return HttpResponse("SUCCESS")

@csrf_exempt
def delete_node(request):
    try: 
        node_to_delete = ClueNode.objects.get(unique_id=request.POST['unique_id'])
        treasure_hunt = TreasureHunt.objects.get(first_node__unique_id=request.POST['unique_id'])
        next_node = node_to_delete.next_node

        if next_node:
            treasure_hunt.first_node = next_node
            treasure_hunt.save()
        else:
            treasure_hunt.delete()
        node_to_delete.delete()
    except:
        return HttpResponse("ERROR")
    return HttpResponse("SUCCESS")

@csrf_exempt
def find_Thunt(request):
    try: 
        user_lat = request.POST['latitude']
        user_long = request.POST['longitude']
        Thunt_list = TreasureHunt.objects.filter(
                first_node__latitude__gt = user_lat - 0.02,
                first_node__latitude__lt = user_lat + 0.02,
                first_node__longitude__gt = user_long - 0.02,
                first_node__longitude__lt = user_long + 0.02
            )
        return Thunt_list
        
    except:
        return HttpResponse("ERROR")
    return HttpResponse("SUCCESS")


def generate_unique_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
