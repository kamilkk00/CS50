# Project 1: Wiki 

This project is a simple, Wikipedia-like online encyclopedia that allows users to browse, search, create, edit, and view encyclopedia entries. Each entry is written in Markdown and rendered as HTML when viewed.

## Video Demo:
[Wiki Demo](https://youtu.be/9XdMzFzk4rY)

## Key Features:
1. **Entry Page**:  
   Users can visit `/wiki/TITLE`, where `TITLE` is the name of an encyclopedia entry, to view its content. If the entry does not exist, the user will see a "page not found" error.

2. **Index Page**:  
   The homepage lists all encyclopedia entries. Each entry is clickable, taking the user to the entry's page.

3. **Search**:  
   Users can search for encyclopedia entries via a search box. If the query matches an entry title, the user is redirected to that entry. If not, a list of all entries containing the search query as a substring is shown.

4. **New Page**:  
   Users can create new encyclopedia entries. If an entry with the same title already exists, an error message is shown. Otherwise, the new entry is saved and displayed.

5. **Edit Page**:  
   Each entry page includes an "Edit" button, allowing users to modify the entry's content. The existing Markdown is pre-loaded into a textarea, where users can make edits. Upon saving, the changes are updated and displayed.

6. **Random Page**:  
   A "Random Page" button allows users to view a random entry from the encyclopedia.

7. **Markdown to HTML Conversion**:  
   All Markdown content is automatically converted to HTML before being displayed to users, ensuring user-friendly formatting.

## Technologies Used:
- **Python**: Backend logic using Django.
- **Django**: Web framework for handling views, URLs, and templates.
- **HTML & CSS**: For structuring and styling the pages.
- **Markdown2**: Used to convert Markdown into HTML for rendering.

## Project Structure:
- **views.py**: Contains logic for rendering and managing encyclopedia entries.
- **models.py**: Defines data models for entries.
- **urls.py**: Manages the routing of different URLs (like index, entry, search, etc.).
- **templates/encyclopedia/**: Contains all the HTML templates used by the app.
- **static/encyclopedia/**: CSS and other static files.
- **util.py**: Contains helper functions for saving, retrieving, and listing entries.
