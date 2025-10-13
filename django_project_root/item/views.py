from django.shortcuts import render, get_object_or_404
from .models import Item

def item_detail(request, pk):
    # item = get_object_or_404(Item, pk=pk, is_sold=False)
    item = get_object_or_404(Item, pk=pk)
    related_items = (
        Item.objects.filter(category=item.category, is_sold=False)
        .exclude(pk=pk)
        .order_by("-created_at")[0:4]
    )
    return render(
        request, "item/item_detail.html", {"item": item, "related_items": related_items}
    )


