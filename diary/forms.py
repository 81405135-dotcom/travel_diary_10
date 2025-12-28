from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'location', 'travel_date', 'story', 'photo']  # photo included
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }

