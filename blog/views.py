from django.shortcuts import render

# Create your views here.
# post_list same name as in blog/urls.py referred to
def post_list(request):
    return render(request, 'blog/post_list.html', {})