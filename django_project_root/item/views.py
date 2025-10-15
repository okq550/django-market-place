from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.http import 
from django.db.models import Q

from .models import Item
from .forms import NewItemForm, EditItemForm


def browse(reequest):
    query = reequest.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(reequest, "item/browse.html", {"items": items, 'query': query})


def detail(request, pk):
    # item = get_object_or_404(Item, pk=pk, is_sold=False)
    item = get_object_or_404(Item, pk=pk)
    related_items = (
        Item.objects.filter(category=item.category, is_sold=False)
        .exclude(pk=pk)
        .order_by("-created_at")[0:4]
    )

    print(f"User: {request.user}, Item User: {item.created_by}")
    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Create an item object and don't commit it to DB since we don't have a user linked to the item yet.
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()
    return render(request, "item/form.html", {"form": form, 'title': 'New Item'})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect("dashboard:index")


@login_required
def edit(request, pk):
    # # Debug: Check if item exists
    # try:
    #     item = Item.objects.get(pk=pk)
    #     print(f"Item exists: {item.name}")
    #     print(f"Created by: {item.created_by}")
    #     print(f"Current user: {request.user}")
    #     print(f"Match: {item.created_by == request.user}")
    # except Item.DoesNotExist:
    #     print(f"No item with pk={pk}")
    #     return HttpResponse(f"No item with ID {pk} exists in database")

    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST" and item.created_by == request.user:
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=pk)
    else:
        form = EditItemForm(instance=item)
    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "Edit Item"
        },
    )
