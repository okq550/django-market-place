from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django_project_root.conversation.models import Conversation, ConversationMessage
from django_project_root.item.models import Item
from .forms import NewConversationMessageForm

@login_required()
def inbox(request):
    # item = Item.objects.filter(created_by=request.user)
    # return render(request, 'conversation/inbox.html', {'item': item})
    pass

@login_required()
def new(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if request.user == item.created_by:
        return redirect('item:detail', pk=item_pk)
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)
    
    if request.method == 'POST':
        form = NewConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation.created_by = request.user
            conversation_message.save()
            return redirect('item:detail', pk=item_pk)

    else:
        form = NewConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': NewConversationMessageForm
    })

@login_required()
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(id=pk)

    if request.method == 'POST':
        form = NewConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation.created_by = request.user
            conversation_message.save()
            return redirect('conversation:detail', pk=pk)

    else:
        form = NewConversationMessageForm()

    return render(request, 'conversation/detail.html', {'conversation': conversation, 'form': form})