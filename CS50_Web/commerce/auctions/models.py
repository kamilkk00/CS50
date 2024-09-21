from django.contrib.auth.models import AbstractUser
from django.db import models

# Crating SQL table for User 
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.id}, User: {self.username}, e-mail: {self.email}, password: {self.password}"

# Creating SQL table for Auction 
class Auction(models.Model):
    category_choice = [
    ('Fashion', 'Fashion'),
    ('Toys', 'Toys'),
    ('Electronics', 'Electronics'),
    ('Home', 'Home'),
    ('Sports', 'Sports'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auction") 
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    starting_bid = models.IntegerField()
    category = models.CharField(max_length=50, choices=category_choice, default='None', blank=True)
    url = models.CharField(max_length=10000, blank=True, null=True)
    avaliable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}, Title of auction: {self.title}, Description of item: {self.description}, Starting Bid: {self.starting_bid}, Categories: {self.category},  URL: {self.url} By: {self.user}"
    
    def username(self):
        return self.user.username

    def auction_title(self):
        return self.title
    
    def auction_description(self):
        return self.description
    
    def auction_starting_bid(self):
        return self.starting_bid
    
    def auction_category(self):
        return self.category
    
    def auction_url(self):
        return self.url
    
    def auction_avaliable(self):
        return self.avaliable
    
    def auction_category(self):
        return self.category

# Crating SQL table for Price 
class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid") 
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bid")
    bid = models.IntegerField()

    def __str__(self):
        return f"Bid: {self.bid} on Auction: {self.auction.title}"
    
    def username(self):
        return self.user.username
    
    def auction_title(self):
        return self.auction.title
    
# Creating SQL table for Comment
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment") 
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"Comment: {self.comment} on Action: {self.auction.title}"

    def username(self):
        return self.user.username
    
    def auction_title(self):
        return self.auction.title
 
# Creating SQL table fo Watchlist
class Watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist") 
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="watchlist")
    liked = models.BooleanField(default=True)

    def __str__(self):
        return f"User: {self.user.username} Liked: {self.auction.title}"
    
    def username(self):
        return self.user.username
    
    def user_liked(self):
        return self.user_liked
    
    def title(self):
        return self.auction.title
