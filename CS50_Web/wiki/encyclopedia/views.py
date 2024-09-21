from django.shortcuts import render, redirect
from . import util
import markdown2
from django.template import TemplateDoesNotExist
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



# Entring to pages via url
def greet(request, page):
    try:
        # Local path needed
        with open(f'"local_path"{page}.md', 'r') as file:
            markdown_text = file.read()
            html = markdown2.markdown(markdown_text)
            page = page.capitalize()
        return render(request, "encyclopedia/web.html",{
            'page' : page,
            'greet' : html
        })
    except (FileNotFoundError, UnboundLocalError, TemplateDoesNotExist):
        return render(request, "encyclopedia/error.html")

# Error page if user do not write /wiki/....
def error(request, page):
    return render(request, "encyclopedia/error.html",{
        "page":page
    })



def search(request):
    try:
        query = request.GET.get('q', '') 

        # logic for search for query that not match full name 
        entries = util.list_entries()
        filtered_entries = [item for item in entries if query in item.lower()]
        for item in entries:
            item = item.lower()
            if query in item and query != item:
                return render(request, f"encyclopedia/search.html",{
                    "entries" : filtered_entries
                })

        # Logic for Search 
        if query:
            """Local path needed""" 
            with open(f'local_path{query}.md', 'r') as file:
                markdown_text = file.read()
                html = markdown2.markdown(markdown_text)
                query = query.capitalize()
            return render(request, "encyclopedia/web.html",{
                'page' : query,
                'greet' : html
            })
        
        # If user do not type anything then function make him back into index
        else:
            return index(request)
        
    except (TemplateDoesNotExist, FileNotFoundError):
        return render(request, "encyclopedia/error.html")

def new(request):
    if request.method == "POST":

        # If user do not write title
        title = request.POST.get("title", "")
        if title == "":
            return render(request, "encyclopedia/errorempty.html")
        content = request.POST.get("content", "")
        title = title.capitalize()

        # lowering letters 
        for item in util.list_entries():
            item = item.lower()
            tit = title.lower()
            
            # checking if title already exist
            if item == tit:
                return render(request, "encyclopedia/errornew.html")
        
            
        # If everything ok then creating new page
        """Local path needed""" 
        with open(f'local_path{title}.md', 'w') as file: 
            file.write(f"{content}")
        
        #opening that page after saving it 
        """Local path needed""" 

        with open(f'local_path{title}.md', 'r') as file:
            markdown_text = file.read()
            html = markdown2.markdown(markdown_text)
            title = title.capitalize()
        return render(request, "encyclopedia/web.html",{
            'page' : title,
            'greet' : html
        })
    
    # if something goes wrong with POST
    return render(request, "encyclopedia/new.html")

def edit(request, page):
    """Local path needed""" 
    content = open(f'local_path{page}.md')
    content = content.read()

    return render (request, "encyclopedia/edit.html",{
        'page': page,
        'content': content
    })

def savig(request):
    if request.method == "POST":
        title = request.POST.get("title_edit", "")
        content = request.POST.get("content_edit", "")

        # checking if title is not empty 
        if title == "":
            return render(request, "encyclopedia/errorempty.html")

        # writing file
        
        """Local path needed""" 
        with open(f'local_path{title}.md', 'w') as file: 
            file.write(f"{content}")
        #return render (request, "encyclopedia/new.html")

        """Local path needed""" 
        with open(f'local_path{title}.md', 'r') as file:
            markdown_text = file.read()
            html = markdown2.markdown(markdown_text)
            title = title.capitalize()
        return render(request, "encyclopedia/web.html",{
            'page' : title,
            'greet' : html
        })

    # if something goes wrong with POST
    return index(render)

# random page funtion
def random_page(request):
    strona = random.choice(util.list_entries())
    return redirect('greet', page=strona)
