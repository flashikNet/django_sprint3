from django.http import Http404
from django.shortcuts import render


def index(request):
    template_name = 'blog/index.html'
    context = {
        'posts': list(reversed(posts))
    }
    return render(request, template_name, context=context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = next(filter(lambda x: x['id'] == id, posts), None)
    if post is None:
        raise Http404(f'Post with id:{id} does not exist')
    context = {
        'post': post
    }
    return render(request, template_name, context=context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = {
        'category': category_slug
    }
    return render(request, template_name, context=context)
