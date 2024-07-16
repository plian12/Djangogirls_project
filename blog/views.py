from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
# create post_list function, take request as argument/parameter

def post_list(request):
    #Create variable called post that grabs all objects 
    # return the request, HTML files you want to send.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})