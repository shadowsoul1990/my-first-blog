from django.shortcuts import render
# dot before models means 'in current directory'
# if models lies somewhere else, absolute path needs to be given instead
from .models import Post
from django.utils import timezone

# Create your views here.
# Basis to show posts in HTML template
# post_list same name as in blog/urls.py referred to
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})