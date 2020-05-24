from django import forms
from django.forms import ModelForm
from blog.models import post,Comment

class PostFrom(ModelForm):

    class Meta:
        model = post
        fields = ('author','title','text',)

        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),

        }

class CommentFrom(ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text',)

        widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
