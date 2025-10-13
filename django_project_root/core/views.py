from django.shortcuts import render
from django_project_root.item.models import Category, Item

def index(request):
    # Get 6 items
    # items = Item.objects.filter(is_sold=False)[0:6]
    items = Item.objects.all()[0:6]
    categories = Category.objects.all()[0:6]
    return render(
        request, "core/index.html", {"items": items, "categories": categories}
    )


def contact(request):
    return render(request, "core/contact.html", {})


def login(request):
    return render(request, "core/login.html", {})
