import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project4.settings')
django.setup()

from network.models import User, Post, Follower, Like

def main():
    x = 0 
    contents = Post.objects.all().order_by("-timestamp")
    posts_with_likes = []
    for content in contents: 

        user_like = Like.objects.all()
        users = []
        for like in user_like:
            users.append({
                "user_name": like.user.username,
                "post_id": like.post.id
            })

        likes = Like.objects.filter(post = content.id)
        likes_count = likes.count()
        like_username = [like.user.username for like in likes]
        posts_with_likes.append({
            "post": content,
            "likes_count": likes_count,
            "like_username": like_username
        })

    for info in users:
        print(info['user_name'], info['post_id'])
    print("")


    print(users)
    print("")
    print(posts_with_likes)
    print("")
    desired_post_id = 16
    username = [user['user_name'] for user in users if user['post_id'] == desired_post_id]
    print(username)


if __name__ == "__main__":
    main()