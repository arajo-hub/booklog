from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from . import models
from account.models import User
from .forms import PostForm
from django.urls import reverse, reverse_lazy

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

class PostList(generic.ListView):
    model = models.Post
    select_related=('user', )
    paginate_by=10
    queryset=Post.objects.all()

class PostDetail(generic.DetailView):
    model=models.Post
    template_name='post/post_detail.html'
    context_object_name='post'

class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url='/login/'
    fields=('title', 'author', 'publisher', 'pubdate', 'review',)
    model=models.Post
    success_url=reverse_lazy('post:all')

class PostDelete(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    login_url='/login/'
    select_related=('user', )
    model=models.Post
    success_url=reverse_lazy('post:all')
