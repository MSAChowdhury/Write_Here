from django.forms import ModelFrom
from .models import post,Comment

class PostFrom(ModelFrom):

    class Meta:
        model = post
        fields = ('author','title','text',)

        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),

        }

class CommentFrom(ModelFrom):

    class Meta:
        model = Comment
        fields = ('author','text',)

        widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
