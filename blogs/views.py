from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blogs.models import Blog, Comment

class HomeView(ListView):
    """
    HomeView: display all blogs with pagination, sorted by updated_on
    """
    model = Blog
    template_name = 'blogs/home.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.all().select_related('author').prefetch_related('comments')


class BlogDetailView(DetailView):
    """
    BlogDetailView: display blog detail with comments and comment form
    """
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().select_related('commenter')
        return context


class BlogCreateView(CreateView):
    """
    BlogCreateView: for creating a new blog (login required)
    """
    model = Blog
    fields = ['title', 'content', 'tag']
    template_name = 'blogs/blog_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class BlogUpdateView(UpdateView):
    """
    BlogUpdateView: for updating a blog (author or admin only)
    """
    model = Blog
    fields = ['title', 'content', 'tag']
    template_name = 'blogs/blog_form.html'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_object(self, queryset=None):
        blog = super().get_object(queryset)
        if self.request.user != blog.author and not self.request.user.is_superuser:
            msg = "You do not have permission to edit this post."
            raise PermissionDenied(msg)
        return blog

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'uuid': self.object.uuid})


class BlogDeleteView(DeleteView):
    """
    BlogDeleteView: for deleting a blog (author or admin only)
    """
    model = Blog
    template_name = "blogs/blog_confirm_delete.html"
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_object(self, queryset=None):
        blog = super().get_object(queryset)
        if self.request.user != blog.author and not self.request.user.is_superuser:
            msg = "You do not have permission to delete this post."
            raise PermissionDenied(msg)
        return blog

    def get_success_url(self):
        return reverse('home')


class CommentCreateView(CreateView):
    """
    CommentCreateView: for adding a comment to a blog (login required)
    """
    model = Comment
    fields = ['content']
    template_name = 'blogs/comment_form.html'

    def form_valid(self, form):
        form.instance.blog = Blog.objects.get(uuid=self.kwargs['uuid'])
        form.instance.commenter = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'uuid': self.kwargs['uuid']})