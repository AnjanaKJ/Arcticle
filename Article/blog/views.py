from django.shortcuts import render,get_object_or_404
from .form import ArticleF
from .models import Article
from django.http import Http404
# Create your views here.

def Article_create(request):
    obj = ArticleF(request.POST or None)
    if obj.is_valid():
        obj.save()
        obj = ArticleF()
    context = {
        "object":obj
    }
    return render(request,"blog/form.html",context)

def details(request,id):
    #obj = Products.objects.get(id = id)  it raises an error if object does not exist so..obj = get_object_or_404(Products,id=id)
    try:
        obj = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    context = {'object':obj}
    return render(request,"blog/detail.html",context)

def all_art(request):
    obj = Article.objects.all()
    context = {
        "obj":obj
    }
    return render(request,"blog/all.html",context)