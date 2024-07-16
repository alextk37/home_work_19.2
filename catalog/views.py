from django.shortcuts import render
from catalog.models import Category, Products
from catalog.models import get_top_categories as top


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
    
    context = {
        "top": top(),
        "title": "Главная",
    }
    return render(request, "index.html", context)


def catalog(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        

    context = {
        "products": Products.objects.all(),
        "title": "Каталог",}
    
    return render(request, "catalog.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        

    return render(request, "contacts.html")

def about_company(request):
    return render(request, "about_company.html")
