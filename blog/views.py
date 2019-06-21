from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 10

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

class CommentView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Comment
    permission_required = 'blog.can_post_comment'
    template_name = 'blog/comment.html'

    def get_queryset(self):
        return Comment.objects.filter().order_by('post_date')