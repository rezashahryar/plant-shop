from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


class CategoryPost(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    category = models.ForeignKey(CategoryPost, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField()
    cover = models.ImageField(upload_to='posts-cover/')
    text = models.TextField()

    published_status = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.author} : {self.title}'
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-datetime_created', )
