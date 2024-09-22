# Network - CS50W Project

This project is a social network website inspired by Twitter, where users can make posts, follow other users, and interact with posts by liking or editing them.

## Video Demo:
[Network Demo](https://www.youtube.com/watch?v=W_34RlwCXMc)

## Key Features:

1. **New Post**:  
   Logged-in users can create a new text-based post. The post will be displayed in reverse chronological order, with the most recent posts appearing first.

2. **All Posts**:  
   Users can view all posts from all users on a dedicated page. Each post displays the username of the poster, the content, the timestamp, and the number of likes.

3. **Profile Page**:  
   Clicking on a username directs the user to that user's profile page, which shows the number of followers and followed users, and a list of all their posts in reverse chronological order.  
   Users can follow or unfollow others directly from their profile pages, except themselves.

4. **Following Page**:  
   Users can view a page showing all posts made by users they are following, with the same features as the "All Posts" page.

5. **Pagination**:  
   Posts are paginated, displaying 10 posts per page. Users can navigate between pages using "Next" and "Previous" buttons.

6. **Edit Post**:  
   Users can edit their own posts. The post's content will be replaced by a text area where changes can be made and saved asynchronously using JavaScript.

7. **Like and Unlike Posts**:  
   Users can like or unlike any post using JavaScript. The like count will be updated asynchronously without refreshing the page.

## Technologies Used:
- **Python**: Backend logic using Django.
- **JavaScript**: For asynchronous page updates (AJAX).
- **Django**: Web framework for handling views, models, and URLs.
- **HTML & CSS**: For structuring and styling the pages.
- **Bootstrap**: For responsive design and pagination.

## Project Structure:
- **models.py**: Defines the data models, including User, Post, Like, and Follow.
- **views.py**: Contains the logic for rendering the posts, handling likes, editing posts, and following/unfollowing users.
- **urls.py**: Manages the URL routes for different pages like index, profile, and following.
- **templates/network/**: HTML templates used by the application for displaying pages.
- **static/network/**: Contains static files like CSS and JavaScript.

## Additional Functionality:
- **Asynchronous Updates**: Liking, unliking, and editing posts are performed asynchronously using fetch requests, providing a smooth user experience.
- **User Authentication**: Users must be logged in to make posts, follow others, and like or edit posts.

This project showcases a simple yet functional social networking platform with core features that resemble those found on modern platforms.
