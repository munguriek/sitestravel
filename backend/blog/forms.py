from django import forms
from blog.models import Category, Comment, Post
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content', )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Blog post title'}))
    content = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].label = "Upload image (formats .png, .jpeg, jpg)"

    class Meta:
        model = Post
        fields = '__all__' 
        exclude = ['author', 'slug', 'status'] 


    