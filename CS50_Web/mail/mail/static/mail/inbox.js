document.addEventListener('DOMContentLoaded', function() {
  
  // Button (inbox) for showing emails 
  document.querySelector('#inbox').addEventListener('click', function(){
    fetch('/emails/inbox')
    .then(response => response.json())
    .then(emails => {
      email(emails)
    });
    load_mailbox('inbox');
  });

  // Button (sent) for showing emails 
  document.querySelector('#sent').addEventListener('click', function(){
    sent()
  }); 

  // Button (archived) for showing emails
  document.querySelector('#archived').addEventListener('click', function(){
    fetch('/emails/archive')
    .then(response => response.json())
    .then(emails => {
      email(emails);
    });
    load_mailbox('archive');
  }); 

  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  def();
});

function compose_email(x = '', y = '', z = '') {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Debuging to make recipients empty one by default 
  if (x instanceof PointerEvent){
    x = '';
  }

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = x;
  document.querySelector('#compose-subject').value = y;
  document.querySelector('#compose-body').value = z;
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}


// Creating interface after reload 
function def(){
  fetch('/emails/inbox')
  .then(response => response.json())
  .then(emails => {
    email(emails)
  });
  load_mailbox('inbox');
}

// function to showing email content 
function email(emails){
  emails.forEach(element => {
    const email_list = document.createElement('div');
    email_list.classList.add("email_detail");
    
    email_list.innerHTML = `
    <div style="flex: 1; text-align: left;"> ${element.sender}</div>
    <div style="flex: 2; text-align: center; font-weight: bold;">${element.subject}</div>
    <div style="flex: 1; text-align: right;">${element.timestamp}</div>`;

    colored(element, email_list);

    // Button for showing detail of email
    email_list.addEventListener('click', () => {
      const email = document.querySelector('#emails-view')

      email.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="flex: 1; text-align: left;"> 
          <span style="font-weight: bold;">  From:</span> ${element.sender}<br> 
          <span style="font-weight: bold;">  To:</span> ${element.recipients}<br> 
        </div>

        <div style="flex: 2; text-align: center;">
          <span style="font-weight: bold;"> Subject:</span> ${element.subject}
        </div>
        <div style="flex: 1; text-align: right;">${element.timestamp}</div> 
      </div> <hr>
      <div style="font-size: 25px;">${element.body} </div><hr> 
      `;

      read(element);
      replay(element);
      archive_button(element);
    });
  
    // Showing all emails 
    document.querySelector("#emails-view").append(email_list);
  });
}


// Sent function 
function sent(){
  fetch('/emails/sent')
  .then(response => response.json())
  .then(emails => {
    emails.forEach(element => {
      const email_list = document.createElement('div');
      email_list.classList.add("email_detail");
    
      email_list.innerHTML = `
      <div style="flex: 1; text-align: left;"> ${element.sender}</div>
      <div style="flex: 2; text-align: center; font-weight: bold;">${element.subject}</div>
      <div style="flex: 1; text-align: right;">${element.timestamp}</div>`;

      // Detail of email
      email_list.addEventListener('click', () => {
        const email = document.querySelector('#emails-view')
        
        email.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div style="flex: 1; text-align: left;"> 
            <span style="font-weight: bold;">  From:</span> ${element.sender}<br> 
            <span style="font-weight: bold;">  To:</span> ${element.recipients}<br> 
          </div>

          <div style="flex: 2; text-align: center;">
            <span style="font-weight: bold;"> Subject:</span> ${element.subject}
          </div>
          <div style="flex: 1; text-align: right;">${element.timestamp}</div> 
        </div> <hr>
        <div style="font-size: 25px;">${element.body} </div><hr>
        `;

      });
      // Showing all emails 
      document.querySelector("#emails-view").append(email_list);
    });
  });
  load_mailbox('sent')
}

// Sending email 
document.addEventListener('DOMContentLoaded', function(){ 
  document.querySelector('form').onsubmit = function(event){
    event.preventDefault();
    const rec = document.querySelector('#compose-recipients').value;
    const sub = document.querySelector('#compose-subject').value;
    const bo = document.querySelector('#compose-body').value;
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: rec,
        subject: sub,
        body: bo,
      })
    })
    .then(response => response.json())
    .then(() => sent())
    //.then(() => load_mailbox('sent'))
  };
});


// Funtion for replaying 
function replay(element){
  const replay = document.createElement('button');
  replay.textContent = 'Replay';
  replay.classList.add('btn', 'btn-sm', 'btn-outline-primary');
  document.querySelector("#emails-view").append(replay);

  replay.addEventListener('click', function(){
    console.log('hello');
    re = element.subject
    if (re.startsWith("Re")){
      re = element.subject
    }
    else{
      re = `Re: ${element.subject}`
    }
    separator = "-".repeat(120)
    compose_email(`${element.sender}`, `${re}`, `\n\n ${separator} \n On ${element.timestamp} ${element.sender} wrote: \n ${element.body}`);
  });
}

// Logic for archive_button
function archive_button(element){
  const archive_button = document.createElement('button');
  archive_button.classList.add('btn', 'btn-sm', 'btn-outline-primary');
  archive_button.style.marginTop = '0px';
  archive_button.style.marginLeft = '15px';

  if (element.archived === false){
    archive_button.textContent = 'Archive';
    archive_button.addEventListener('click', () => {
      fetch(`/emails/${element.id}`,{
        method: 'PUT',
        body: JSON.stringify({
          archived: true
        })
      })
      .then (() =>{
        def(); 
        location.reload()
      })
    });
  } else {
    archive_button.textContent = 'Unarchived';
    archive_button.addEventListener('click', () => {
      fetch(`/emails/${element.id}`,{
        method: 'PUT',
        body: JSON.stringify({
          archived: false
        })
      })
      .then (() =>{
        def(); 
        location.reload();
      })
    });
  }
  document.querySelector("#emails-view").appendChild(archive_button);

}

// Changing for read:true after user go into email 
function read(element){
  fetch(`/emails/${element.id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read : true
    })
  })
}

// Function which take care of color if email is read or not  
function colored(element, email_list){
  if (element.read === true){
    email_list.style.backgroundColor = '#f0f0f0';
  }
  else{
    email_list.style.backgroundColor = 'white';
  }
}
