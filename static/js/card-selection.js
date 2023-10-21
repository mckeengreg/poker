// Call the function when the page loads
initializeActiveCards();


// Get the cards container
const cardsContainer = document.querySelectorAll('.cards');

// Add an event listener to the cards container
cardsContainer.forEach(container => {
	container.addEventListener('click', function(event) {
	    let cardElement = null;

	    // Check if a card or its children were clicked
	    if (event.target.classList.contains('card')) {
	        cardElement = event.target;
	    } 
	    else if (event.target.closest('.card')) {
	        cardElement = event.target.closest('.card');
	    }

	    if (cardElement) {
	        // Using the ID of the cardElement to get the associated checkbox
	        const checkboxName = cardElement.id;
	        const checkbox = document.querySelector(`input[data-name="${checkboxName}"]`);
	        
	        // Toggle the checkbox's checked state
	        checkbox.checked = !checkbox.checked;

	        // Add or remove the "active" class based on the checkbox's state
	        if (checkbox.checked) {
	            cardElement.classList.add('active');
	        } else {
	            cardElement.classList.remove('active');
	        }

	        // Use AJAX to submit the form
	        submitFormAjax();
	    }
	});
});

// This function adds the 'active' class to cards with checkboxes that are already checked
function initializeActiveCards() {
    const checkboxes = document.querySelectorAll('.cards input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            const cardElement = checkbox.closest('.card');
            cardElement.classList.add('active');
        }
    });
    submitFormAjax();
}


function submitFormAjax() {
    const formData = new FormData(cardForm);
    const responseMessageDiv = document.getElementById('responseMessage');

    fetch(cardForm.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  // Assuming server responds with json
    .then(data => {
        // Update the div with the returned message
        responseMessageDiv.textContent = data.message;
        if (data.winning_set) {
        	responseMessageDiv.textContent += ' ' + data.winning_set + '!';
        }
        
        // Optionally, you can add or remove classes based on the status to style the message
        if (data.status === "success") {
            responseMessageDiv.classList.add('success-message');
            responseMessageDiv.classList.remove('error-message');
        } else {
            responseMessageDiv.classList.add('error-message');
            responseMessageDiv.classList.remove('success-message');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
