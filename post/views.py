from django.shortcuts import render
from .models import Post
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models

def save(request):
    if request.method == "POST":
        post=Post.objects.all()
        context={'Post' : post}
        try :
            post=Post(user=request.user,
            title=request.POST['title'],
            author=request.POST['author'],
            publisher=request.POST['publisher'],
            pubdate=request.POST['pubdate'],
            review=request.POST['review'])
            post.save()
        except:
            post=None
        return render(request, 'booklog/index.html', context)

def edit(request, pk):
    post=Post.objects.get(id=pk)
    print(pk)
    if request.method == "POST":
        post=Post.objects.all()
        context={'Post' : post}
        try :
            if post.review != request.POST['review']:
                post=Post(user=request.user,
                title=request.POST['title'],
                author=request.POST['author'],
                publisher=request.POST['publisher'],
                pubdate=request.POST['pubdate'],
                review=request.POST['review'])
                post.save()
            else:
                messages.error("You didn't edit this post")
        except:
            post=None
        return render(request, 'booklog/index.html', context)

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user',)
