
// Get the cards container
const cardsContainer = document.querySelector('.cards');

// Add an event listener to the cards container
cardsContainer.addEventListener('click', function(event) {
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
