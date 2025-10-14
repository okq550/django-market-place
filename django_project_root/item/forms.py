from django import forms
from .models import Item

INPUT_CLASS = 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            })
        }