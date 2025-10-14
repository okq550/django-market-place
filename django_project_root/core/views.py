from django.shortcuts import render, redirect
from django_project_root.item.models import Category, Item
from .forms import SignUpForm, SignInForm


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


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            redirect('core.home')
    else: 
        form = SignInForm()
    return render(request, "core/signin.html", {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core/signin')
    else:
        form = SignUpForm()
    return render(request, "core/signup.html", {"form": form})
