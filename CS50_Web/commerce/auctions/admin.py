from django.contrib import admin

from .models import User ,Auction, Bid, Comment, Watchlist

class BidAdmin(admin.ModelAdmin):
    list_display = ( "bid", "username", "auction_title", )
admin.site.register(Bid, BidAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ( "username", "auction_title", "comment")
admin.site.register(Comment, CommentAdmin)

class AuctionAdmin(admin.ModelAdmin):
    list_display = ( "auction_avaliable", "username", "auction_title",  "auction_starting_bid", "auction_category", "auction_description", "auction_url"   )
admin.site.register(Auction, AuctionAdmin)

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ( "username", "title" ,"liked")
admin.site.register(Watchlist, WatchlistAdmin)


admin.site.register(User)
