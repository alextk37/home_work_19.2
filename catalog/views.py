from django.shortcuts import render

def catalog(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'({name} : {email}) - {message}')

    return render(request, "catalog.html")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'({name} : {email}) - {message}')

    return render(request, "contacts.html")

