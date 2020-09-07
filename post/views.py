from django.shortcuts import render
from .models import Post

def save(request):
    if request.method == "POST":
        post=Post.objects.all()
        context={'Post' : post}
        try :
            post=Post(title=request.POST['title'],
            author=request.POST['author'],
            publisher=request.POST['publisher'],
            pubdate=request.POST['pubdate'],
            review=request.POST['review'])
            post.save()
        except:
            post=None
        return render(request, 'home.html', context)
