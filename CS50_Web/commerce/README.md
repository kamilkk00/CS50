# Project 3: Commerce

This project is an e-commerce auction platform that allows users to create listings, place bids, comment on listings, and manage watchlists. It is built using Django and provides a full-featured online auction system.

## Video Demo:
[Commerce Demo](https://www.youtube.com/watch?v=Yx3fN8dZxjM)

## Key Features:

1. **Create Listings**:  
   Users can create new auction listings by specifying a title, description, starting bid, category, and an optional image URL. The listings are then displayed on the homepage.

2. **Active Listings**:  
   The homepage displays all currently active auction listings. Each listing includes the title, current bid, description, and image if available. Users can click on a listing to view more details.

3. **Listing Page**:  
   - **Place Bids**: Users can place bids on the listing, provided the bid is higher than the current price.  
   - **Add/Remove from Watchlist**: Users can add or remove the listing from their personal watchlist.  
   - **Comment on Listing**: Users can leave comments on the listing.  
   - **Close Auction**: If they are the creator of the listing, they can close the auction, making the highest bidder the winner.

4. **Watchlist**:  
   Users can add auction listings to their personal watchlist. The watchlist page displays all items that the user is watching, and users can remove items from the list.

5. **Categories**:  
   Users can filter active listings by category. Clicking on a category shows all auctions under that category.

6. **Bidding and Auction Closing**:  
   Users can place bids on active listings. Once the auction is closed, the highest bidder wins the auction, and the listing becomes inactive.

7. **Commenting**:  
   Users can leave comments on auction listings, and all comments are displayed on the listing’s detail page.

8. **Django Admin Interface**:  
   The site administrator can view, add, edit, and delete any listings, bids, or comments through the Django admin interface.


## Technologies Used:
- **Python**: Backend logic using Django.
- **JavaScript**: For interactive functionality.
- **Django**: Web framework for handling views, models, and routes.
- **HTML & CSS**: For structuring and styling the platform.
- **Bootstrap**: For responsive design and layout.

## Project Structure:
- **models.py**: Defines the database models for auction listings, bids, comments, and users.
- **views.py**: Contains the logic for handling requests and rendering the appropriate templates.
- **urls.py**: Maps the app’s routes to the correct views.
- **templates/auctions/**: Contains HTML templates for rendering the pages of the auction site.
- **static/auctions/**: Holds static files like CSS and JavaScript for styling and front-end interactions.

## Additional Functionality:
- **User Authentication**: Users must register and log in to create listings, place bids, and manage their watchlists.
- **Admin Management**: Site administrators can manage auctions, bids, and user comments through the Django admin interface.
te 
