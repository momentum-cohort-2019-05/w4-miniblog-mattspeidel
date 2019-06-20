from django.shortcuts import render

# Create your views here.
from blog.models import Blog, Blogger, Comment

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()

    num_bloggers = Blogger.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_comments = Comment.objects.count()
    
    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_comments': num_comments,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)