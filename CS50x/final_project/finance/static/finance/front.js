document.addEventListener('DOMContentLoaded', function(){
    const saveButtons = document.getElementById('saveButton');
    const postIDElement = document.getElementById('postID')
    const userElement = document.getElementById('user_name')
    const logout = document.getElementById('logout')

    if (logout){
        logout.addEventListener('click', function(){
            alert("You have successfully logged out.")
        });
    }

    // Ensure elements exist before using them
    if (saveButtons && postIDElement && userElement){
        const postID = postIDElement.textContent.split(':')[1];
        const user = userElement.textContent.trim();
        saveButtons.addEventListener('click', function(){
            check_if_save(postID, user, saveButtons);
        });
    }

    // Function to like the post
    const like_button = document.getElementById("likeButton");
    if (like_button && userElement && postIDElement) {
        like_button.addEventListener('click', function(){
            const user = userElement.textContent.trim();
            const postID = postIDElement.textContent.split(':')[1];      
            liking_post(postID, user);
        });
    }

    // Function to like the comment
    if (userElement) {
        document.querySelectorAll('[id^="commentLike-"]').forEach(button => {
            const user = userElement.textContent.trim();
            button.addEventListener('click', function(){
                like_comment(this, user);
            });
        });
    }

    // Function to edit the post
    const edit_button = document.getElementById("edit_post");
    if (edit_button) {
        edit_button.addEventListener('click', function(){
            edit_post(edit_button);
        });
    }

    // Function to edit the comment
    const edit_comment_buttons = document.querySelectorAll(".edit_comment");
    edit_comment_buttons.forEach(button => {
        button.addEventListener('click', function(){
            edit_comment(button);
        });
    });
});



// Function to check if the post is saved or not
function check_if_save(postID, user, saveButtons){
    fetch(`/saved/post/detail/${postID}`)
    .then(response => response.json())
    .then(data => {
        const saved_post = data.find(saved_post => saved_post.user === user);

        if(saved_post){
            // If the post has been saved
            if(saveButtons.textContent === 'Save'){
                fetch(`/detail/save/post/${postID}`,{
                    method: 'PUT', 
                    header: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: user,
                        post_id: postID,
                        if_save: true
                    })
                });
                saveButtons.textContent = "Unsave";
                saveButton.classList.remove("btn-info");
                saveButton.classList.add("btn-warning");                
            }
            // If the post has not been saved
            else{
                fetch(`/detail/save/post/${postID}`,{
                    method: 'PUT',
                    header:{
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: user,
                        post_id: postID,
                        if_save: false
                    })
                });
                saveButtons.textContent = 'Save'
                saveButton.classList.remove("btn-warning");
                saveButton.classList.add("btn-info");
            }
        }
        // If the post never has been saved
        else{
            fetch(`/detail/save/post/${postID}`,{
                method:'POST',
                header:{
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: user, 
                    post_id: postID,
                    if_save: true    
                })
            });
            saveButtons.textContent = 'Unsave'
            saveButton.classList.remove("btn-info");
            saveButton.classList.add("btn-warning");

        }
    });
};

// Function to like the post
function liking_post(postID, user){
    const likeButton = document.getElementById("likeButton")
    const like_count_all = document.getElementById("like_counting")
    const like_count = like_count_all.getAttribute('data-like-count')
    const like_liczba = parseInt(like_count, 10);

    fetch(`/detail/like/post/${postID}`)
    .then (response => response.json())
    .then(likes => {    
        const user_liked = likes.some(like => like.user === user);
        if (user_liked){
            const check_like = likes.find(like => like.user === user)
            // Unlike if the user has liked the post before
            if (check_like.if_like === true){
                fetch(`/save/like/${postID}`,{
                    method:'PUT', 
                    header:{
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: user, 
                        post_id : postID,
                        if_like: false
                    })
                })
                likeButton.textContent = "Like"
                likeButton.classList.remove("btn-danger");
                likeButton.classList.add("btn-success");
                const number = like_liczba - 1;
                like_count_all.setAttribute('data-like-count', number)
                like_count_all.innerHTML = `<strong>Likes:</strong> ${number}`;
            }
            // Like if the user has liked the post before
            else{
                fetch(`/save/like/${postID}`,{
                    method: 'PUT', 
                    header:{
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: user, 
                        post_id : postID,
                        if_like: true
                    })
                })
                likeButton.textContent = "Unlike"
                likeButton.classList.remove("btn-success");
                likeButton.classList.add("btn-danger");
                const number = like_liczba + 1;
                like_count_all.setAttribute('data-like-count', number)
                like_count_all.innerHTML = `<strong>Likes:</strong> ${number}`;
            }
        }
        // Like if the user has never liked the post before
        else{
            fetch(`/save/like/${postID}`,{
                method: "POST",
                header:{
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    post_id : postID,
                    username : user,
                    if_like: true
                })
            })
            likeButton.textContent = "Unlike"
            likeButton.classList.remove("btn-success");
            likeButton.classList.add("btn-danger");
            const number = like_liczba + 1;
            like_count_all.setAttribute('data-like-count', number)
            like_count_all.innerHTML = `<strong>Likes:</strong> ${number}`;

        }
    });
};

// Function to like the comment
function like_comment(button, user){
    const commentId = button.getAttribute('data-comment-id');

    const like_count_all = document.getElementById(`like_counting_comment_${commentId}`);
    const like_count = like_count_all.getAttribute('data-like-comment')
    const like_liczba = parseInt(like_count, 10);

    fetch(`/detail/comment/like/post/${commentId}`)
    .then(response => response.json())
    .then(data => {
        const userLiked = data.some(comment => comment.user === user);
        if(userLiked){
            // Like if the user has liked the comment before
            if(button.textContent === "Like"){
                fetch(`/save/comment/like/${commentId}`,{
                    method: 'PUT',
                    body: JSON.stringify({
                        username: user, 
                        comment_id : commentId,
                        if_like: true
                    })
                })
                button.textContent = "Unlike";
                button.classList.remove("btn-success");
                button.classList.add("btn-danger");

                const number = like_liczba + 1;
                like_count_all.setAttribute('data-like-comment', number)
                like_count_all.innerHTML = `<strong>Likes:</strong> ${number}`;

            }
            // Unlike if the user has liked the comment before
            else{
                fetch(`/save/comment/like/${commentId}`,{
                    method: 'PUT', 
                    body: JSON.stringify({
                        username: user,
                        comment_id : commentId,
                        if_like: false
                    })
                })
                button.textContent = "Like";
                button.classList.remove("btn-danger");
                button.classList.add("btn-success");

                const number = like_liczba - 1;
                like_count_all.setAttribute('data-like-comment', number)
                like_count_all.innerHTML = `<strong>Likes:</strong> ${number}`;
            }
        }
        // Like if the user has never liked the comment before
        else{
            fetch(`/save/comment/like/${commentId}`,{
                method: "POST",
                body: JSON.stringify({
                    username: user, 
                    comment_id: commentId,
                    if_like: true
                })
            })
            button.textContent = "Unlike";
            button.classList.remove("btn-success");
            button.classList.add("btn-danger");

            const number = like_liczba + 1;
            like_count_all.setAttribute('data-like-comment', number)
            like_count_all.innerHTML = `<strong>Likes:</strong> ${number}`;

        }
    })
};
// Function to edit the post
function edit_post(edit_button){

    const edit_content = document.getElementById('edit_content');
    const post_id = edit_button.getAttribute('data-post-id');

    const post_content_element = document.querySelector('.post-content');

    if(edit_button.textContent.trim() === "Edit"){

        // Create a text area to edit the post
        const post_content = edit_content.getAttribute('data-edit-content');
        const text_area = document.createElement('textarea');


        text_area.style.fontSize = '22.4px';
        text_area.style.lineHeight = '35.84px';
        text_area.style.maxWidth = '100%'; 

        text_area.style.width = '1050px';   
        text_area.style.padding = '20px';
        text_area.style.margin = '40px auto';
        text_area.style.backgroundColor = '#fff';
        text_area.style.borderRadius = '8px';
        text_area.style.boxShadow = '0 0 15px rgba(0, 0, 0, 0.1)';
        text_area.style.border = '1px solid #ddd';
        text_area.style.height = '300px';
    
        edit_content.innerHTML="";
        post_id.innerHTML = "";
        post_content_element.innerHTML = "";

        text_area.value = post_content;

        document.getElementById("edit_content").append(text_area);

        edit_button.textContent = "Save";   
             
    }
    else{

        const text_area = edit_content.querySelector('textarea');
        if(text_area){
            const user_input = text_area.value;
            
            edit_content.setAttribute('data-edit-content', user_input);

            // Updating the post with the new content, and sending it into the database
            fetch(`/save/edit/post/${post_id}`,{
                method: 'PUT',
                body: JSON.stringify({
                    content: user_input
                })
            })
            
        }
        text_area.remove();
        edit_button.textContent = "Edit"

        // Refresh the page to see the changes
        window.location.reload() 
        window.location.reload() 
        window.location.reload() 
        window.location.reload() 
        window.location.reload() 
        window.location.reload() 
        window.location.reload() 

    }
};


// Function to edit the comment
function edit_comment(element){
    const comment_id = element.getAttribute('data-comment-id');
    const comment_all = document.getElementById(`comment_content_${comment_id}`);
    const comment_content = comment_all.getAttribute('data-comment-content');
    const button_content = element.textContent.trim();

    // Create a text area to edit the comment
    if(button_content === "Edit"){
        comment_all.innerHTML = "";
        const text_area = document.createElement('textarea');
        text_area.value = comment_content;
        comment_all.append(text_area);
        element.innerHTML = "Save";
    }
    // Save the edited comment
    else{
        const text_area = comment_all.querySelector('textarea');
        if(text_area){
            const user_input = text_area.value;
            comment_all.innerHTML = `${user_input}`; 
            fetch(`/save/edit/comment/${comment_id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    content: user_input
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    // Successfully saved
                    element.innerHTML = 'Edit';
                } else {
                    // Handle error response
                    console.error(data.error);
                }
            });
        }    
    }
}