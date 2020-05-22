from django import forms
from blog.models import post,Comment

class PostFrom(froms.ModelFrom):

    class Meta():
        model = post
        fields = ('author','title','text')

        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }

class CommentFrom(forms.ModelFrom):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
