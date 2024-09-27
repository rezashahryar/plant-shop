from django import forms

from . models import Comment

# create your forms here


class PostCommentForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Comment
        fields = ['text']
