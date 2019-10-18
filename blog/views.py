from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Blog


def index(request):
    # return HttpResponse('Hello ')
    return render(request, 'index.html')

def allBlogs(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': list(blogs),
        'name': 'Rahil Memosasasn'
    }
    return render(request, 'allblog.html', context)


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'detail.html', {
        'blog': blog
    })
