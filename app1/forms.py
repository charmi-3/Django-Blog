from django import forms
from .models import *

choices= Category.objects.all().values_list('name','name')

choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
 class Meta:
    model = Post
    fields = ('title','author','body','category')
    widgets = {
        'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
        'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
        'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
        'body': forms.Textarea(attrs={'class':'form-control','placeholder':''}),
    }
class EditForm(forms.ModelForm):
 class Meta:
    model = Post
    fields = ('title','body',)
    widgets = {
        'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
        'body': forms.Textarea(attrs={'class':'form-control','placeholder':''}),
    }
