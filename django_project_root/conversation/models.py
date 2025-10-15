from django.contrib.auth.models import User
from django.db import models
from django_project_root.item.models import Item

class Conversation(models.Model):
    # item.conversations.all() - all conversations for an item
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    # user.conversations.all() - all conversations a user participated in
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at', )

class ConversationMessage(models.Model):
    # conversation.messages.all() - all messages in a conversation
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
