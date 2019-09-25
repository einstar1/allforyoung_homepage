from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        
        return context


# def index(request):
#    posts = Post.objects.all()
#
#    return render(
#        request,
#        'blog/index.html',
#        {
#            'posts': posts,
#        }
#    )