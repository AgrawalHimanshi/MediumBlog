from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        'title': "Blog 1",
        'author': "John Doe",
        'content': "my forst blog",
        "date_posted":"30 March 2020",
    },
    {
        'title': "Blog 2",
        'author': "John Doe",
        'content': "my forst blog",
        "date_posted":"30 March 2020",
    }
]
def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
