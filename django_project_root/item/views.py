from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import NewItemForm

def detail(request, pk):
    # item = get_object_or_404(Item, pk=pk, is_sold=False)
    item = get_object_or_404(Item, pk=pk)
    related_items = (
        Item.objects.filter(category=item.category, is_sold=False)
        .exclude(pk=pk)
        .order_by("-created_at")[0:4]
    )
    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Create an item object and don't commit it to DB since we don't have a user linked to the item yet.
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'item/new.html', {
        'form': form
    })