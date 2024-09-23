document.getElementById('sentimentForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent form submission

    // Get the review input
    const review = document.getElementById('reviewInput').value;

    // Make a POST request to Flask API
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ review: review }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the sentiment result
        document.getElementById('sentiment').textContent = data.sentiment;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
