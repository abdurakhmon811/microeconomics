from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from .assistants import Police
from .models import About, \
    Blog, \
    File

import re

def index(request: HttpRequest):
    """
    Renders the main page.
    """

    main_info = None
    try:
        main_info = About.objects.latest('date_time')
    except ObjectDoesNotExist:
        pass

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


def blog(request: HttpRequest, blog_title: str):
    """
    Renders the page for checking a blog in detail.
    """

    post = get_object_or_404(Blog, title=blog_title)
    context = {
        'post': post,
    }
    return render(request, 'main/blog.html', context)


def publish_blog(request: HttpRequest):
    """
    Adds a blog post.
    """

    police = Police()
    police.check_superuser(request)
    if request.method == 'POST':
        publisher = request.user
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        body = request.POST.get('body')
        print(body)
        conclusion = request.POST.get('conclusion')
        sources = request.POST.get('sources')
        data = Blog.objects.all()
        blog_titles = [each.title for each in data]
        if title in blog_titles:
            raise PermissionDenied
        else:
            new_post = Blog.objects.create(
                                        publisher=publisher,
                                        title=title,
                                        subtitle=subtitle,
                                        body=body,
                                        conclusion=conclusion,
                                        sources=sources,
                                    )
            new_post.save()
            return redirect('blogs')


def delete_blog(request: HttpRequest, blog_title: str):
    """
    Deletes the chosen blog post.
    """

    police = Police()
    police.check_superuser(request)
    post = get_object_or_404(Blog, title=blog_title)
    post.delete()
    return redirect('blogs')


def files(request: HttpRequest):
    """
    Renders the files page where also clients can download the desired file.
    """

    docs = File.objects.all()

    context = {
        'docs': docs,
    }
    return render(request, 'main/files.html', context)


def add_file(request: HttpRequest):
    """
    Adds the POSTed file into the database (not the file itself but its name, description and location).
    """

    # For now, the police guard has very limited methods on security
    police = Police()
    police.check_superuser(request)
    if request.method == 'POST':
        file_name = request.POST.get('name')
        file_description = request.POST.get('description')
        file_link = request.POST.get('link')
        data = File.objects.all()
        file_names = [each.name for each in data]
        if file_name in file_names:
            raise PermissionDenied
        else:
            new_file = File.objects.create(name=file_name, description=file_description, link=file_link)
            new_file.save()
            return redirect('files')


def delete_file(request: HttpRequest, file_name: str):
    """
    Deletes the chosen file.
    """

    police = Police()
    police.check_superuser(request)
    target = get_object_or_404(File, name=file_name)
    target.delete()
    return redirect('files')



def search(request: HttpRequest):
    """
    Renders the page with found items matched the requested name.
    """
    
    searched = None
    files = None
    posts = None
    if request.method == 'GET' and 'searched' in request.GET:
        searched = request.GET.get('searched')
        if re.fullmatch('bosh sahifa', searched, flags=re.IGNORECASE):
            return redirect('index')
        elif re.fullmatch('maqolalar', searched, flags=re.IGNORECASE):
            return redirect('blogs')
        elif re.fullmatch('fayllar', searched, flags=re.IGNORECASE):
            return redirect('files')
        elif re.fullmatch('ramazonov-shamil-login', searched, flags=re.IGNORECASE):
            return redirect('ramazonov_shamil_login')
        else:
            files = File.objects.filter(Q(name__icontains=searched) | 
                                        Q(description__icontains=searched))
            posts = Blog.objects.filter(Q(title__icontains=searched) | 
                                        Q(subtitle__icontains=searched) | 
                                        Q(body__icontains=searched) | 
                                        Q(conclusion__icontains=searched))
    
    context = {
        'searched': searched,
        'files': files,
        'posts': posts,
        'not_found': True if not files and not posts else False,
    }
    return render(request, 'main/search.html', context)


def ramazonov_shamil_login(request: HttpRequest):
    """
    Logs the superuser in.
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            raise PermissionDenied
    
    return render(request, 'registration/login.html')


def logout_superuser(request: HttpRequest):
    """
    Logs the superuser out.
    """

    logout(request)
    return redirect('index')
