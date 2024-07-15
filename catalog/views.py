from django.shortcuts import render


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'({name} : {email}) -> {message}')
    return render(request, "index.html")


def catalog(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'({name} : {email}) -> {message}')
    
    return render(request, "catalog.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'({name} : {email}) -> {message}')

    return render(request, "contacts.html")

def about_company(request):
    return render(request, "about_company.html")
