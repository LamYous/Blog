from django.db import models
from django.contrib.auth.models import User

# Models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('-created_at',)

    # def comment_count(self):
    #     return self.comment_set.all().count()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.content
    
    

