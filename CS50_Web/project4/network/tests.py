from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, User, Follower, Like

# Create your tests here.
class PostTest(TestCase):

    # Seting up objects
    def setUp(self):
        y1 = User.objects.create(
            username = "testuser",
            email = "testemail@o2.pl",
            password = "test"
        )
        x1 = "Hello, how you are doung"
        post1 = Post.objects.create(user= y1 , post=x1)

        y2 = User.objects.create(
            username = "user",
            email = "email@o2.pl",
            password = "user"
        )
        x2 = "What's app"
        post2 = Post.objects.create(user= y2 , post=x2)

        Follower.objects.create(user = y1, follower = y2, if_follow = True)
        Follower.objects.create(user= y2, follower=y1, if_follow = False)

        Like.objects.create(user = y1, post= post1, if_like = False)
        Like.objects.create(user = y2, post= post2, if_like = True)
        Like.objects.create(user = y1, post= post1, if_like = True)


    # checking if post posted 
    def test_count(self):
        count = Post.objects.all()
        self.assertEqual(count.count(), 2)

    # Cheking if posts are valid
    def test_valid_post(self):
        valid = Post.objects.all().first()
        self.assertTrue(valid.is_valid_post())
    
    # Cheking if invalid posts are invalid
    def test_invalid_post(self):
        invalid = Post.objects.all().first()
        self.assertFalse(invalid.is_invalid_post())
        
    # Testing if site is working
    def test_index(self):
        c = Client()
        response = c.get("")
        self.assertEqual(response.status_code, 200)

    def test_user(self):
        user = User.objects.all().first()
        user_x = user.username
        c = Client()
        url = reverse('about', args=[user_x])
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        user = User.objects.all()
        user = user[1]
        user_y = user.username
        c = Client()
        url = reverse('about', args=[user_y])
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    # Testing if follower correctly created in databases 
    def test_follow(self):
        count = Follower.objects.all()
        self.assertEqual(count.count(), 2)

    # Testing if Follow is valid 
    def test_valid_follow(self):
        valid = Follower.objects.all().first()
        self.assertTrue(valid.is_valid_follower())

    # Testing if Follow is invalid 
    def test_valid_follow(self):
        valid = Follower.objects.all().first()
        self.assertFalse(valid.is_invalid_follower())


    # Testing if Likes correctly created in databases 
    def test_likes(self):
        count = Like.objects.all()
        self.assertEqual(count.count(), 3)

    # Testing if Like is valid
    def test_valid_like(self):
        valid= Like.objects.all().first()
        self.assertTrue(valid.is_valid_like())

    # Testing if like is invalid
    def test_invalid_like(self):
        invalid = Like.objects.all().first()
        self.assertFalse(invalid.is_invalid_like())

