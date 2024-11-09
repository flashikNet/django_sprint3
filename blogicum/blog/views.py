from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    template_name = 'blog/index.html'
    posts = Post.objects.select_related(
        "category", "location", "author"
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by("-pub_date")[:5]
    context = {
        'post_list': posts
    }
    return render(request, template_name, context=context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post, pk=id)
    if (not post.category.is_published
            or not post.is_published
            or post.pub_date > timezone.now()):
        raise Http404()
    context = {
        'post': post
    }
    return render(request, template_name, context=context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404()
    posts = Post.objects.select_related(
        "category", "author", 'location'
    ).filter(
        category__id=category.pk,
        is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, template_name, context=context)
