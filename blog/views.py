from django.shortcuts import render, get_object_or_404
from .models import BlogProject
def all_blogs(request):
    blog_projects = BlogProject.objects.all()
    return render(request, 'blog/all_blogs.html', {'blog_projects':blog_projects})

def detail(request, blog_id):
    blog = get_object_or_404(BlogProject, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
