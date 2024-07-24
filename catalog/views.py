from django.shortcuts import render
from catalog.models import Category, Products


def index(request):
    context = {
        "top": Products.objects.all().order_by("-view_count")[:3],
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
        "title": "Каталог",
    }

    return render(request, "catalog.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
    context = {
        "title": "Контакты",
    }

    return render(request, "contacts.html", context)


def about_company(request):
    return render(request, "about_company.html")


def product_item(request, pk):
    context = {
        "product": Products.objects.get(pk=pk),
        "title": Products.objects.get(pk=pk).product_name,
    }
    return render(request, "product_item.html", context)


def new_product(request):
    context = {
        "title": "Новый продукт",
        "categories": Category.objects.all(),
    }
    if request.method == "POST":
        product_name = request.POST.get("productName")
        description = request.POST.get("productDescription")
        preview_img = request.FILES.get("productImage")
        category_id = request.POST.get("productCategory")
        price = request.POST.get("productPrice")

        category = Category.objects.get(pk=category_id)

        new_product = Products(
            product_name=product_name,
            description=description,
            preview_img=preview_img,
            category=category,
            price=price,
        )
        new_product.save()
    return render(request, "new_product.html", context)
