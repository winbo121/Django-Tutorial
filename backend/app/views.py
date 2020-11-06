from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django_test.models import *
import datetime

def test(request):

    return render(request,'template/test.html')



@csrf_exempt
def book_list(request):
    context=dict()

    books = Book.objects.all()
    book_list = []

    for book in books:
      book_list.append({'id': book.id, 'book_name': book.book_name, 'created_at': book.created_at})


    context['data']=book_list

    return JsonResponse(context)


@csrf_exempt
def book_create(request):
    context=dict()
    book_name = request.POST.get('book_name')

 
    Book(book_name=book_name,created_at=datetime.datetime.now()).save()

    context['data']='success'

    return JsonResponse(context)

@csrf_exempt
def book_update(request):
    context=dict()

    book_name = request.POST.get('book_name')
    book = Book.objects.get(book_name=book_name)
    book.created_at =datetime.datetime.now()
    book.save()

    context['data']='success'

    return JsonResponse(context)

@csrf_exempt
def book_delete(request):
    context=dict()
    book_name = request.POST.get('book_name')
    
    book = Book.objects.get(book_name=book_name)
    book.delete()


    context['data']='success'
   

    return JsonResponse(context)