from django.contrib import admin
from blog.models import Blog, Blogger, Comment

# Register your models here.
# admin.site.register(Blog)
# admin.site.register(Blogger)
# admin.site.register(Comment)

class BloggerAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Blogger, BloggerAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'author')

admin.site.register(Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post_date', 'post_time', 'comment', 'commenter')

admin.site.register(Comment, CommentAdmin)