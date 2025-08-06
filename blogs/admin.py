from django.contrib import admin
from blogs.models import Blog, Comment

admin.site.register(Blog)
admin.site.register(Comment)

class BlogAdmin(admin.ModelAdmin):
    """
    BlogAdmin: admin interface for Blog model
    """
    list_display = ['title', 'author', 'tag', 'created_on', 'updated_on']
    list_filter = ['tag', 'created_on', 'author']
    search_fields = ['title', 'content', 'tag']
    readonly_fields = ['uuid', 'created_on', 'updated_on']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author')


class CommentAdmin(admin.ModelAdmin):
    """
    CommentAdmin: admin interface for Comment model
    """
    list_display = ['get_blog_title', 'commenter', 'created_on']
    list_filter = ['created_on', 'commenter']
    search_fields = ['content', 'blog__title', 'commenter__username']
    readonly_fields = ['uuid', 'created_on', 'updated_on']
    
    def get_blog_title(self, obj):
        return obj.blog.title
    get_blog_title.short_description = 'Blog Title'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('blog', 'commenter')