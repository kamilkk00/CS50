from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

 
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.id}, User: {self.username}, e-mail: {self.email}, password: {self.password}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    id = models.AutoField(primary_key=True)
    post = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id}, User: {self.user.username}, Post:{self.post}, Added: {self.timestamp}"
    
    def is_valid_post(self):
        return self.post != "" and self.user is not None
    
    def is_invalid_post(self):
        return self.post == "" or self.user is None
    
class Follower(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folow")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folower")
    if_follow = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id}, User: {self.user.username}, Folower: {self.follower.username}, Following: {self.if_follow}"
    
    def is_valid_follower(self):
        return self.follower is not None and self.user is not None
    
    def is_invalid_follower(self):
        return self.follower is None or self.user is None 
      
class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like")
    if_like = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}, User: {self.user.username}, Post: {self.post.id}, Like: {self.if_like}"
    
    def is_valid_like(self):
        return self.user is not None and self.post is not None 
    
    def is_invalid_like(self):
        return self.user is None or self.post is None 