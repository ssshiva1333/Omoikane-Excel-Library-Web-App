from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from . import excelAPI

def mainPageView(request):
    if request.method == "GET":
        books = excelAPI.excelAPI.getBook()

        return render(request, "main.html", {"books":  books})
    else:
        return HttpResponseBadRequest("404 Not Found")

def excelAPIAdd(request):
    if request.method == "POST":
        book = {
                'bName': request.POST.get('bName'),
                'aName': request.POST.get('aName'),
                'pNumber': request.POST.get('pNumber'),
                'genre': request.POST.get('genre'),
                'eNumber': request.POST.get('eNumber'),
                'pName': request.POST.get('pName')
        }
        
        excelAPI.excelAPI.addBook(book)

        return redirect("main")
    else:
        return HttpResponseBadRequest("405 Invalid HTTP method.")
    
def excelAPIChange(request):
    if request.method == "POST":
        book = {
                'bName': request.POST.get('bName'),
                'aName': request.POST.get('aName'),
                'pNumber': request.POST.get('pNumber'),
                'genre': request.POST.get('genre'),
                'eNumber': request.POST.get('eNumber'),
                'pName': request.POST.get('pName')
        }
        
        excelAPI.excelAPI.changeBook(book)

        return redirect("main")
    else:
        return HttpResponseBadRequest("405 Invalid HTTP method.")

def excelAPIRemove(request):
    if request.method == "POST":
        book = {
                'bName': request.POST.get('bName'),
                'aName': request.POST.get('aName'),
                'pNumber': request.POST.get('pNumber'),
                'genre': request.POST.get('genre'),
                'eNumber': request.POST.get('eNumber'),
                'pName': request.POST.get('pName')
        }
        
        excelAPI.excelAPI.removeBook(book)

        return redirect("main")
    else:
        return HttpResponseBadRequest("405 Invalid HTTP method.")

def excelAPIGet(request):
    if request.method == "GET":
        book = {
                'bName': request.GET.get('bName'),
                'aName': request.GET.get('aName'),
                'pNumber': request.GET.get('pNumber'),
                'genre': request.GET.get('genre'),
                'eNumber': request.GET.get('eNumber'),
                'pName': request.GET.get('pName')
        }
        
        print(book)
        books = excelAPI.excelAPI.getBook(book)
                
        return render(request, "main.html", {"books": books})
    else:
        return HttpResponseBadRequest("405 Invalid HTTP method.")
    
def excelAPIBackup(request):
    if request.method == "GET":
        excelAPI.excelAPI.excelBackup()
        
        return redirect("main")
    else:
        return HttpResponseBadRequest("405 Invalid HTTP method.")