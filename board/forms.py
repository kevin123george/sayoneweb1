from django import forms

from .models import Board_element

class Board_elementForm(forms.ModelForm):
    class Meta:
        model = Board_element
        fields = ('title','description','technology',)
        widgets = {
            'description' : forms.Textarea(attrs={'placeholder':'description'}),
        }




