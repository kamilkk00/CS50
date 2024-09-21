from django.contrib import admin
from .models import User, Post, Follower, Like


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Follower)
admin.site.register(Like)