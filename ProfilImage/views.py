from django.shortcuts import render
from django.http import JsonResponse
from .forms import (CitizenForm)
from asgiref.sync import sync_to_async

# Create your views here.


async def Home(request):
    return render(request, 'index.html', {'form': CitizenForm()})


@sync_to_async
def SaveProfile(request):
    Obj_Form = CitizenForm(request.POST, request.FILES)
    print("##################### : ", Obj_Form, Obj_Form.is_valid())
    if Obj_Form.is_valid():
        Obj = Obj_Form.save()
        return JsonResponse(Obj.Json())
    else:
        return JsonResponse({'message': [{'name': key, 'message': value} for key, value in Obj_Form.errors.items()]})
