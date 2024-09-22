# Project 3: Mail

This project is an email client that allows users to send, receive, and manage emails through a web-based interface. The client functions as a single-page application, using JavaScript to send and receive data from the server without requiring full-page reloads.

## Video Demo:
[Mail Demo](https://youtu.be/3rikJXhMqVY)

## Key Features:

1. **Send Mail**:  
   Users can compose and send emails by filling out a form with the recipient, subject, and body. The sent emails are stored in the "Sent" mailbox, and users can view them after submission.

2. **Mailbox Views**:  
   Users can navigate between three mailboxes: Inbox, Sent, and Archive. Each mailbox displays emails with details such as sender, subject, and timestamp. Emails are sorted in reverse chronological order, and unread emails are highlighted.

3. **View Email**:  
   Users can click on an email to view its full contents, including sender, recipients, subject, timestamp, and body. Once an email is opened, it is marked as read.

4. **Archive and Unarchive Emails**:  
   Users can archive emails from the inbox and move them to the Archive mailbox. Similarly, users can unarchive emails, moving them back to the inbox.

5. **Reply to Emails**:  
   Users can reply to received emails. The recipient field is pre-filled with the original sender’s address, and the subject is automatically prefixed with "Re:". The original email’s content is included in the reply.

## Technologies Used:
- **Python**: Backend logic using Django.
- **JavaScript**: For asynchronous page updates (AJAX).
- **Django**: Web framework for handling views, models, and URLs.
- **HTML & CSS**: For structuring and styling the pages.
- **Bootstrap**: For responsive design and layout.

## Project Structure:
- **models.py**: Contains models representing emails and user interactions.
- **views.py**: Handles the API routes for sending, receiving, and updating email data.
- **urls.py**: Maps the app’s routes to the appropriate views.
- **inbox.js**: Contains the JavaScript logic for managing the front-end interactions, including sending and retrieving emails and updating the UI.
- **templates/mail/**: HTML templates used for rendering the email client interface.
- **static/mail/**: Contains static files like CSS and JavaScript for styling and front-end behavior.

## Additional Functionality:
- **Asynchronous Updates**: Sending and receiving emails, as well as archiving and replying, are handled asynchronously using fetch requests to the API.
- **User Authentication**: The system requires users to register and log in to send and receive emails.
