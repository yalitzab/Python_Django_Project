from django.shortcuts import render 
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'This is the content of blog post 1.',
        'date_posted': 'August 27, 2023'
        # Uncomment the line below to use a different date format
        # 'date_posted': '2023-10-01'
    },
    {
        'author': 'Jane Smith',
        'title': 'Blog Post 2',
        'content': 'This is the content of blog post 2.',
        'date_posted': 'August 28, 2023'
        # 'date_posted': '2023-10-02'
    }
]

#logic to routes

def home(request):
    # This function renders the home page of the blog by creating a Key
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# def login(request):
#     # This function renders the login page of the blog
#     return render(request, 'blog/login.html', {'title': 'Login'})

def about(request):
    # This function renders the about page of the blog
    return render(request, 'blog/about.html', {'title': 'About'})


