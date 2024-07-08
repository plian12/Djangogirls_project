from django.shortcuts import render

# Create your views here.
# create post_list function, take request as argument/parameter

def post_list(request):
    # return the request, HTML files you want to send.
    return render(request, 'blog/post_list.html', {} )