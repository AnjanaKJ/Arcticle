from django import forms
from .models import Article

class ArticleF(forms.ModelForm):

    class Meta:
        model = Article
        fields = ["name","email","des"]