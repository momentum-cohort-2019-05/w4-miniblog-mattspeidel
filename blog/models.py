from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, time


# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text='Enter your blog text')
    post_date = models.DateField(null=True, blank=True, default=date.today)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this post"""
        return reverse('blog-detail', args=[str(self.id)])

class Blogger(models.Model):

    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text='Enter a bio')

    def __str__(self):
        return self.name.username

    def get_absolute_url(self):
        """Returns the url to access a particular blogger instance."""
        return reverse('blogger-detail', args=[str(self.id)])

class Comment(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(null=True, blank=True, default=date.today)
    post_time = models.TimeField(null=True, blank=True, auto_now=True)
    comment = models.TextField(max_length=300, help_text='Enter comment about blog here.')
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.comment

    class Meta:
        
        permissions = (("can_post_comment", "Post comment"),)  

    
