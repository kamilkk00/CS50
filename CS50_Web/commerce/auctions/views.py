from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Auction, Comment, Watchlist, Bid


def index(request):
    auctions = Auction.objects.all()
    auction_bids = []

    for auction in auctions:
        bid = Bid.objects.filter(auction=auction).order_by("-bid").first()
        auction_bids.append({
            'auction': auction,
            'bid': bid
        })

    return render(request, "auctions/index.html", {
        "auction_bids": auction_bids
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    # Adding item to SQL
    if request.method == "POST":

        # Reciving information 
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        category = request.POST["category"]
        url = request.POST["url"]

        #Adding information
        auction = Auction.objects.create(
            user = request.user,
            title=title, 
            description=description, 
            starting_bid=starting_bid, 
            category = category,
            url=url)
        auction.save()

        return HttpResponseRedirect(reverse("index"))


    return render(request, "auctions/create.html")


def auction_detail(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    comments = Comment.objects.filter(auction=auction)
    bid = Bid.objects.filter(auction=auction)
    message = None 
    x = "Add To Watchlist"
    winner= None

    # Helping with biggest price
    z = 0
    for bid in bid:
        if bid.bid >= auction.starting_bid:
            if z < bid.bid: 
                z = bid.bid
        winner = Bid.objects.filter(auction=auction).order_by("-bid").first().user.username


    # Checking if item is in watchlist 
    if request.user.is_authenticated:
        watchlist_filter = Watchlist.objects.filter(user=request.user, auction=auction)

        if Watchlist.objects.filter(user=request.user, auction=auction).exists():
            x = "Remove From Watchlist"
    else: 
        watchlist_filter = None

    # Adding comments
    if request.method == "POST":

        # If user is not loged 
        if not request.user.is_authenticated:
            if request.POST.get("action") == "comment":
                message = "You need to be logged in to add a comment!"
            elif request.POST.get("action") == "watchlist":
                message = "You need to be logged in to add to watchlist"
            elif request.POST.get("action") == "n_bid":
                message = "You need to be logged in to bid this item"
            return render(request, "auctions/item.html", {
                "message": message,
                "auction": auction,
                "comments": comments,
                "x": x,
            })
        
        # Creating bid and checking if is correct 
        if request.POST.get("action") == "n_bid":
            n_bid = request.POST.get("n_bid", "")
            n_bid = int(n_bid)
            highest_bid = max([bid.bid for bid in Bid.objects.filter(auction=auction)] + [0])
            if n_bid > highest_bid:
                if n_bid >= auction.starting_bid:
                    message = "Your Bid is currently the highest"
                    Bid.objects.create(
                        user = request.user,
                        auction = auction,
                        bid = int(n_bid),
                    )
                    bid = Bid.objects.filter(auction=auction)
                    z = max([bid.bid for bid in Bid.objects.filter(auction=auction)] + [0])
                else:
                    message = "Bid must be at least high as the starting bid"
            else:
                message = "Bid must be higher than currect highest bid"

            if Bid.objects.filter(auction=auction).exists():
                winner = Bid.objects.filter(auction=auction).order_by("-bid").first().user.username

            return render(request, "auctions/item.html", {
                "auction": auction,
                "comments": comments,
                "message": message, 
                "x" : x,
                "bid": bid,
                "z": z,
                "winner": winner
            })


        # Checking if item is in watchlist and adding if is not 
        if request.POST.get("action") == "watchlist":
            if Watchlist.objects.filter(user=request.user, auction=auction).exists():
                watchlist_filter.delete()
            else:
                Watchlist.objects.create(
                    user = request.user,
                    auction = auction,
                )
            return redirect("auction_detail", auction_id=auction_id)

        # Adding comment
        if request.POST.get("action") == "comment":
            comment = request.POST.get("comment", "")
            new_comment = Comment.objects.create(
                user = request.user,
                auction = auction,
                comment = comment,
            )
            new_comment.save()
            return redirect("auction_detail", auction_id=auction_id)
        
        if request.POST.get("action") == "end_auction":
            auction.avaliable = False
            auction.save()
        return redirect("auction_detail", auction_id=auction_id)

    # Checking if item is still avaliable 
    if auction.avaliable == False:
        if request.user.username == winner:
            message = "You won this item. Congratulations!"
        else:
            message = "This item is no longer available for sale"

    # Showing auction
    return render(request, "auctions/item.html", {
        "auction": auction,
        "comments": comments,
        "message": message, 
        "x" : x,
        "bid": bid,
        "z": z,
        "winner":winner,
    })


def watchlist(request):

    # Communicat if user is not logged 
    if not request.user.is_authenticated: 
        message= "You need to be log in to see items in watchlist"
        return render(request, "auctions/index.html",{
            "auctions": Auction.objects.all(),
            "message" : message
        })

    # Providing data from SQL 
    user = request.user
    watchlist = Watchlist.objects.filter(user=user)

    return render(request, "auctions/watchlist.html",{
        "user": user,
        "watchlist": watchlist 
    })

# Function for categories 
def categories(request):
    return render(request, "auctions/categories.html",{
        "auction": Auction.objects.all()
    })

# Showing items in specific categories 
def kategorie(request, auction_category):
    auction = Auction.objects.filter(category=auction_category)
    category = auction_category
    return render(request, "auctions/kategorie.html",{
        "auction": auction,
        "category": category,
    })
    