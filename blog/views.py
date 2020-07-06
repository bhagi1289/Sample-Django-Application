from django.shortcuts import render
from django.http import  HttpResponse

from .models import Post
#Dummy Data
# posts = [
#     {
#         'author':'Bhagyaraju',
#         'title':'Blog Post 1',
#         'content':'First post Content',
#         'date_posted':'August 27 2019'
#     },
# {
#         'author':'Corey MS',
#         'title':'Blog Post 2',
#         'content':'Second post Content',
#         'date_posted':'August 30 2019'
#     },
# {
#         'author':'Professor',
#         'title':'Blog Post 3',
#         'content':'Third post Content',
#         'date_posted':'August 27 2019'
#     },
# ]
# Create your views here.


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # return  HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})

