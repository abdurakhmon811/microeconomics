from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from .models import About, \
    Blog, \
    File

import re

def index(request: HttpRequest):
    """
    Renders the main page.
    """

    main_info = About.objects.latest('date_time')

    context = {
        'main_info': main_info,
    }
    return render(request, 'main/index.html', context)


def blogs(request: HttpRequest):
    """
    Renders the blogs page.
    """

    posts = Blog.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'main/blogs.html', context)


def blog(request: HttpRequest, blog_title):
    """
    Renders the page for checking a blog in detail.
    """

    try:
        post = get_object_or_404(Blog, title=blog_title)
    except ObjectDoesNotExist:
        pass
    else:
        context = {
            'post': post,
        }
    
    return render(request, 'main/blog.html', context)


def files(request: HttpRequest):
    """
    Renders the files page where also clients can download the desired file.
    """

    docs = File.objects.all()

    context = {
        'docs': docs,
    }
    return render(request, 'main/files.html', context)


def search(request: HttpRequest):
    """
    Renders the page with found items matched the requested name.
    """

    if request.method == 'GET' and 'searched' in request.POST:
        searched = request.POST.get('searched')
        if re.fullmatch('bosh sahifa', searched, flags=re.IGNORECASE):
            return redirect('index')
        elif re.fullmatch('maqolalar', searched, flags=re.IGNORECASE):
            return redirect('blogs')
        elif re.fullmatch('fayllar', searched, flags=re.IGNORECASE):
            return redirect('files')
        else:
            posts = Blog.objects.filter(Q(title=searched) | 
                                        Q(subtitle=searched) | 
                                        Q(body=searched) | 
                                        Q(conclusion=searched))
            files = File.objects.filter(Q(name=searched) | 
                                        Q(description=searched))
    
    context = {
        'posts': posts,
        'files': files,
    }
    return render(request, 'main/search.html', context)
