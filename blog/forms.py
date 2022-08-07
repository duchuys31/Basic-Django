from django import forms
from .models import comment

class comment_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        cmt = super().save(commit=False)
        cmt.author = self.author
        cmt.post = self.post
        cmt.save()

    class Meta:
        model = comment
        fields = ["body"]
