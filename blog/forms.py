from django import forms

from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-group", 'placeholder': "What's on your mind?"}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': "form-group"}), required=False)
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-group", 'placeholder': "describe your photo"}), required=False)

    class Meta:
        model = Post
        fields = ['message', 'image', 'description']


class CommentAddForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Add comment"}))

    class Meta:
        model = Comment
        fields = ['text']
