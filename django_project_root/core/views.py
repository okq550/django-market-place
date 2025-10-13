from django.shortcuts import render, get_object_or_404
from .models import Category, Item


def index(request):
    # Get 6 items
    # items = Item.objects.filter(is_sold=False)[0:6]
    items = Item.objects.all()[0:6]
    categories = Category.objects.all()[0:6]
    return render(request, "core/index.html", {'items': items, 'categories': categories})


def item_detail(request, pk):
    # item = get_object_or_404(Item, pk=pk, is_sold=False)
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'core/item_detail.html', {'item': item})

def contact(request):
    return render(request, "core/contact.html", {})


def login(request):
    return render(request, "core/login.html", {})


