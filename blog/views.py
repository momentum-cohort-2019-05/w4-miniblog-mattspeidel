from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse


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
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

class CommentView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Comment
    permission_required = 'blog.can_post_comment'
    template_name = 'blog/comment_form.html'

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment']
        
    def form_valid(self, form):
        form.instance.commenter = self.request.user
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context        

    def get_success_url(self): 
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})