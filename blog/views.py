from django.shortcuts import render
from .models import BlogProject
def all_blogs(request):
    blog_projects = BlogProject.objects.all()
    return render(request, 'blog/all_blogs.html', {'blog_projects':blog_projects})
