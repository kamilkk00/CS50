from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Post, Follower, Like
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):

    # Adding new post 
    if request.method == "POST":
        user = request.user
        post = request.POST["description"]
        new_post = Post.objects.create(
            user = user,
            post = post,
            timestamp = timezone.now()
        )
        new_post.save()
        return HttpResponseRedirect(reverse("index"))

    contents = Post.objects.all().order_by("-timestamp")

    # Likes 
    posts_with_likes = []

    for content in contents: 
        likes_count = Like.objects.filter(post = content.id, if_like=True).count()
        users = list(Like.objects.filter(post=content.id, if_like=True).values_list('user__username', flat=True))
        posts_with_likes.append({
            "post": content,
            "likes_count": likes_count, 
            "users": users
        })

    # pagins 
    paginator = Paginator(posts_with_likes, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "contents" : page,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

# Taking care of about website 
def about(request, user_username):
    if not request.user.is_authenticated:
        folower_user = None
    else:
        folower_user = request.user

    user_ = User.objects.filter(username = user_username).first()
    posts = Post.objects.filter(user = user_).order_by("-timestamp")

# Following: 
    # Couting Follower and Following 
    follower_instance = None

    if folower_user:
        follower_instance = Follower.objects.filter(user = user_, follower = folower_user).first()
    count_followers = Follower.objects.filter(user = user_, if_follow = True).count()
    count_following = Follower.objects.filter(follower = user_, if_follow = True).count()
    x = 0

    # Function to prevent of following itself 
    if folower_user == user_:
        x = 3

    # Function for following and saving it in databeses 
    if request.method == "POST" and folower_user:
        folower_user = request.user
        if follower_instance:
            if follower_instance.if_follow:
                follower_instance.if_follow = False
                x = 2
            else:
                follower_instance.if_follow = True
            follower_instance.save()
        else:
            Follower.objects.create(user=user_, follower=folower_user, if_follow=True)

        return redirect('about', user_username=user_username)

    else:
        if follower_instance:
            if follower_instance.if_follow:
                x = 2


    # likes 
    posts_with_likes = []

    for content in posts: 
        likes_count = Like.objects.filter(post = content.id, if_like=True).count()
        users = list(Like.objects.filter(post=content.id, if_like=True).values_list('user__username', flat=True))
        posts_with_likes.append({
            "post": content,
            "likes_count": likes_count, 
            "users": users
        })

    # pagination
    paginator = Paginator(posts_with_likes, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)



    return render(request, "network/user.html",{
        "user_about" : user_,
        "x" : x,
        "count_followers": count_followers,
        "count_following": count_following,
        "contents": page, 
    })

# Function taking care of following
def following(request):
    user = request.user
    following = Follower.objects.filter(follower = user, if_follow = True)
    posts = Post.objects.filter(user__in = following.values('user')).order_by("-timestamp")

    # Logic for likes 
    posts_with_likes = []
    for content in posts: 
        likes_count = Like.objects.filter(post = content.id, if_like=True).count()
        users = list(Like.objects.filter(post=content.id, if_like=True).values_list('user__username', flat=True))
        posts_with_likes.append({
            "post": content,
            "likes_count": likes_count, 
            "users": users
        })

    # Paginator
    paginator = Paginator(posts_with_likes, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)


    return render(request, "network/following.html", {
        "user": user,
        "posts": page
    })

# Function showing detail of all posts 
def json_view(request):
    data = list(Post.objects.values())
    return JsonResponse(data, safe=False)


# Function with show detail of post by id 
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {
        'id' : post.id,
        'user': post.user.username,
        'post': post.post,
        'timestamp': post.timestamp,
    }
    return JsonResponse(data, safe=False)

# Function for saving changes via edit button 
@csrf_exempt
def save_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get("id")
        content = data.get("content")
        post = Post.objects.get(id= post_id)
        post.post = content
        post.save()
        return JsonResponse({'status': 'success'})

# Function for showing all likes 
def show_like(request):
    data = list(Like.objects.values())
    return JsonResponse(data, safe=False)

# function fow showing like detail per id 
def like_detail(request, post_id):
    likes = Like.objects.filter(post_id=post_id)
    data = []
    for like in likes: 
        data.append ({
            "user": like.user.username,
            "post": post_id,
            "if_like": like.if_like
        })
    return JsonResponse(data, safe=False)

# Function for likes in databases very important 
@csrf_exempt
def save_like(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_name = data.get("user_name")
        post_id = data.get("post_id")
        if_like = data.get("if_like")
        like_data = Like.objects.get(post_id = post_id, user__username = user_name)
        like_data.if_like = if_like
        like_data.save()
    return JsonResponse({'status': 'success'})

# Function to creating likes in databases 
@csrf_exempt
def create_like(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_name = data.get("user_name")
        post_id = data.get("post_id")
        if_like = data.get("if_like")
        user = User.objects.get(username=user_name)
        post = Post.objects.get(id = post_id)
        like_data = Like.objects.create(
            user = user,
            post = post,
            if_like = if_like
        )
        like_data.save()
    return JsonResponse({'status': 'success'})

# Function for changing likes in databases 
@csrf_exempt
def change_like(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_name = data.get("user_name")
        post_id = data.get("post_id")
        if_like = data.get("if_like")
        user = User.objects.get(username=user_name)
        post = Post.objects.get(id = post_id)
        like_data = Like.objects.get(user = user, post = post)
        like_data.if_like = if_like
        like_data.save()
        return JsonResponse({"status": "success"})