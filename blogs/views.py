from django.shortcuts import render
from codingoBlogs.views import session_Required
from .models import Blog, BlogCategory, Tags
from django.core.paginator import Paginator
# Create your views here.
@session_Required
def blogs(request):
    try:
        __context = {}
        data = Blog.objects.filter(is_active=True)
        __context['category'] = BlogCategory.objects.filter(is_active=True)
        if request.method == "GET":
            if 'search' in request.GET:
                data = Blog.objects.filter(is_active=True, name__contains = request.GET['search'])
            
        paginator = Paginator(data, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        __context['data'] = page_obj
        __context['range'] = paginator.page_range
        __context['session'] = request.session['LoggedInCustomer']
        return render(request, 'blogs.html',__context)
    except Exception as error:
        return render(request, 'error.html',{"error":error})


@session_Required
def blogDetails(request, url):
    try:
        __context = {}
        data = Blog.objects.get(url=url)
       
        __context['blog'] = data
        __context['category'] = BlogCategory.objects.filter(is_active=True)
        __context['session'] = request.session['LoggedInCustomer']
        return render(request, 'blogDetails.html',__context)
    except Exception as error:
        return render(request, 'error.html',{"error":error})

@session_Required
def blogByCategory(request, id):
    try:
        __context = {}
        data = Blog.objects.filter(is_active=True,category__id=id)

        if request.method == "GET":
            if 'search' in request.GET:
                data = Blog.objects.filter(is_active=True, name__contains = request.GET['search'])
            
        paginator = Paginator(data, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        __context['data'] = page_obj
        __context['range'] = paginator.page_range
        __context['category'] = BlogCategory.objects.filter(is_active=True)
        __context['session'] = request.session['LoggedInCustomer']
        return render(request, 'blogs.html',__context)
    except Exception as error:
        return render(request, 'error.html',{"error":error})