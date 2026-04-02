document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    const text = document.getElementById('text').value;
    fetch('http://localhost:8000/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});