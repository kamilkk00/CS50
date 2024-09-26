# Financial Forum Application
## [Explore the Live Application](https://www.expertbizforum.com/)

The Financial Forum Application is an online platform built using the Django framework, aimed at fostering knowledge sharing between professionals like tax advisors, accountants, and business consultants, and individuals seeking business-related advice. The application serves as a bridge between knowledge seekers and experienced professionals, allowing users to engage with informative content, build professional connections, and access advisory services.

## Video Demo:  
[Finance Forum](https://youtu.be/Eq32tfheDWo)

## Application Overview:

This online forum was designed with the idea of sharing knowledge among experienced individuals or specialists in their respective fields (such as tax advisors, accountants, and others).

Financial Forum is a web application based on the Django framework.  
The forum is intended to serve two types of users.  
The first group consists of people seeking knowledge in a specific area related to running a business. These users will be able to find articles of interest to them. They will also have the ability to view the profile of the person who created the article and potentially gain additional information about them, such as a website or phone number, which would allow them to access an expert in the relevant field.  
The second group consists of specialists who want to share their knowledge. If these individuals provide advisory services (e.g., accounting), they can upgrade their profile to a professional user, where they can provide information about their experience and basic details. After reading an article, users may be interested in using the services of that advisor.

The platform offers many features, such as creating professional profiles with details about experience. All posts can be saved, and authors can edit them. Additionally, there is the option to comment on and like both posts and comments.  
Likes play an important role as they determine the ranking on the homepage.  
Users can also search for articles of interest based on categories or keywords, both by title and content.  
Professional profiles also allow users to leave reviews, including satisfaction ratings (from 1 to 5).

## Features

- **Registration and Login**: Users can register, log in, and log out.
- **Post Creation**: Logged-in users can create new posts in selected categories.
- **Commenting**: Users can comment on posts and edit their comments.
- **User Profiles**: Ability to view profiles of other users, including professional profiles.
- **Professional Profiles**: Users can upgrade their accounts to professional profiles, providing detailed information about their services.
- **Saving and Liking Posts**: Users can save posts for later viewing and add likes.
- **Searching**: Users can search for posts by title or content.
- **Adding Reviews**: Users can add reviews and ratings for professional profiles.

## Project Structure

- **views.py**: Contains the application's logic, including handling post creation, comments, user profiles, and other functions.
- **models.py**: Defines data models such as User, Post, Comment, ProfessionalUser, Like, Save_Post, etc.
- **urls.py**: Defines URL paths for the various views.
- **templates/finance**: Contains HTML templates for the application, including the homepage, login, registration, post creation, user profiles, etc.
- **static/finance**: Contains static files such as CSS and JavaScript used in the application.
