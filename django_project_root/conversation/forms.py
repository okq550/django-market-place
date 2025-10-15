from django import forms
from .models import ConversationMessage

INPUT_CLASS = 'w-full px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none'

class NewConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'rows': 1,
                'placeholder': 'Type a message...'
            }),
        }