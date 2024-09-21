document.addEventListener('DOMContentLoaded', function(){
    
    // Frontend for editing contents 

    const editButtons = document.querySelectorAll('button[id^="button_edit_"]')

    editButtons.forEach(button =>{
        button.onclick = function(){

            // Download ID from button 
            const contentId = this.id.split('_')[2];
            const textareaId = `unique_textarea_${contentId}`;
            const postContainerId = `post_id_${contentId}`;
            const pEditId = `p_edit_${contentId}`;  
            
            if (this.innerHTML === "Edit"){
                if (!document.querySelector(`#${textareaId}`)){
                    const x = document.createElement('textarea');
                    x.id = textareaId;
                    const all_id = document.getElementById(postContainerId);
                    const number_id = parseInt(all_id.textContent, 10);
                    
                    email(number_id).then(email_detail => {
                        x.value = email_detail;
                    });
            
                    this.innerHTML = "Save";
                    document.getElementById(pEditId).append(x);
                    const div_id = document.getElementById(`text_edit_${contentId}`);
                    div_id.style.display = 'none'; 
                    x.style.width = '100%';
                    x.style.marginBottom = '20px';
                }
            }
            else{
                const new_text = document.getElementById(textareaId);
                const text_value = new_text.value;

                
                const all_id = document.getElementById(postContainerId);
                const number_id = parseInt(all_id.textContent, 10);

                const div_id = document.getElementById(`text_edit_${contentId}`);
                div_id.innerHTML = `${text_value}`
                div_id.style.display = 'block'

                saveContent(text_value, number_id)
                new_text.remove();
                this.innerHTML = "Edit";
            }
        };
    });

    const like_button = document.querySelectorAll("button[id^='button_like_']")
    like_button.forEach(button =>{
        button.onclick = function(){
            let x = 0; 
            const button_id = this.id.split('_')[2];
            const username_element = document.getElementById('username');
            const user_clear = username_element.textContent.trim();
            fetch(`/show_like/${button_id}`)
            .then(response => response.json())
            .then(likes => { 
                for (let i = 0; i < likes.length; i++){
                    if (likes[i].user === user_clear){
                        x = 1;
                    }
                }
            if (x === 1){
                if (this.innerHTML.includes("Unlike")){
                    fetch("/change_like/",{
                        method:"POST",
                        body: JSON.stringify({
                            user_name: user_clear,
                            post_id: button_id,
                            if_like: false
                        })
                    })
                    this.classList.remove('btn-outline-danger');
                    this.classList.add('btn-outline-success');
                    this.innerHTML = `<i class="fa fa-heart"></i>Like`;
                    like_count_minus(button_id)


                }
                else{
                    fetch("/change_like/",{
                        method:"POST",
                        body: JSON.stringify({
                            user_name: user_clear,
                            post_id: button_id,
                            if_like: true
                        })
                    })
                    this.classList.remove('btn-outline-success');
                    this.classList.add('btn-outline-danger');
                    this.innerHTML = `<i class="fa fa-heart"></i>Unlike`;
                    like_count_add(button_id)

                }    
            }
            // Creating new like into databases 
            else{
                fetch("/create_like/",{
                    method: "POST", 
                    body: JSON.stringify({
                        user_name: user_clear,
                        post_id: button_id,
                        if_like: true
                    })
                })
                this.classList.remove('btn-outline-success');
                this.classList.add('btn-outline-danger');
                this.innerHTML = `<i class="fa fa-heart"></i>Unlike`;
                like_count_add(button_id)
            }

            });    
        };
    });


});

// Function for checking data of post 
function email(number_id){
    return fetch(`/data-url/${number_id}`)
    .then(response => response.json())
    .then(data => {        
        return data.post;
    });
}

// Function for saving 
function saveContent(text_value, number_id){
    fetch('/save-data/', {
        method: "POST",
        body: JSON.stringify({
            id: number_id,
            content: text_value
        })
    })
    .then(response => response.json())
    .then(data =>{
    });
}


// counting likes without reload of website 
function like_count_add(button_id){
    const old_count_element = document.getElementById(`count_like_${button_id}`);
    const old_count = parseInt(old_count_element.textContent.trim(), 10) || 0;
    const new_count = old_count + 1;
    old_count_element.textContent = new_count

}
function like_count_minus(button_id){
    const old_count_element = document.getElementById(`count_like_${button_id}`);
    const old_count = parseInt(old_count_element.textContent.trim(), 10) || 0;
    const new_count = old_count - 1;
    old_count_element.textContent = new_count
 
}
