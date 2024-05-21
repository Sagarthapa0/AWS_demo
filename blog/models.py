from django.db import models
from user.models import User

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    like=models.ManyToManyField(User,related_name="like",blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment
    
