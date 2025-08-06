import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Blog(models.Model):
    """
    Blog model with UUID primary key, title, content, tag, author, and timestamps
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'uuid': self.uuid})

    def get_content_preview(self, words=30):
        """Return a preview of the content with limited words"""
        content_words = self.content.split()
        if len(content_words) > words:
            return ' '.join(content_words[:words]) + '...'
        return self.content


class Comment(models.Model):
    """
    Comment model with UUID primary key, content, blog reference, commenter, and timestamps
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.commenter.username} on {self.blog.title}'