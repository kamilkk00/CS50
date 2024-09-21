document.addEventListener('DOMContentLoaded', function() {
    const bookingForms = document.querySelectorAll('.list-group-item form');
    const slotsContainer = document.querySelector('.list-group');
    const confirmationMessage = document.createElement('p');

    confirmationMessage.className = 'alert alert-success';
    confirmationMessage.textContent = 'Your booking has been confirmed!';

    // Possibility to book a time slot and confirm the reservation
    bookingForms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); 

            const formData = new FormData(form);
            const actionUrl = form.getAttribute('action');

            const selectedDate = form.querySelector('input[name="date"]').value;
            formData.append('date', selectedDate); 

            fetch(actionUrl, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {  
                    slotsContainer.innerHTML = '';  
                    slotsContainer.appendChild(confirmationMessage);  
                    setTimeout(() => {
                        window.location.reload();
                    }, 3000);
                } else {
                    alert('There was an error with your booking. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    // Hiding the message after 5 seconds
    const messageContainer = document.getElementById('message-container');
    if (messageContainer) {
        setTimeout(() => {
            messageContainer.style.display = 'none';
        }, 3000);  
    }
});