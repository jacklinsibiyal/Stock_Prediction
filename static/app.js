document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const openPrice = document.getElementById('openPrice').value;
    const predictionElement = document.getElementById('prediction');
    const button = this.querySelector('button');

    // Disable the button and show loading state
    button.disabled = true;
    button.textContent = 'Predicting...';
    predictionElement.textContent = '--.--';

    const data = { Open: parseFloat(openPrice) };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        if (result.error) {
            predictionElement.textContent = 'Error';
            alert(result.error);
        } else {
            // Animate the prediction value
            animateValue(predictionElement, 0, result.prediction, 1000);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        predictionElement.textContent = 'Error';
        alert('An error occurred. Please try again.');
    })
    .finally(() => {
        // Re-enable the button and reset its text
        button.disabled = false;
        button.textContent = 'Predict';
    });
});

function animateValue(element, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = progress * (end - start) + start;
        element.textContent = value.toFixed(2);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    document.getElementById("openPrice").value = "";
    window.requestAnimationFrame(step);
}
