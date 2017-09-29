from django.shortcuts import render, get_object_or_404
from .models import Post


def posts_home(request):
    queryset = Post.objects.all()
    # instance = get_object_or_404(Post, id=1)

    query = request.GET.get("bookSearch")
    if query:
        queryset = queryset.filter(title__icontains=query)

    # instance = get_object_or_404(Post, title__icontains=query)
    context = {
        # "book_list": instance,
        # "title": instance.title,
        #"instance": instance,
        "queryset": queryset,
    }

    return render(request, 'searchlayout.html', context)


def book_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, 'bookdetails.html', context)