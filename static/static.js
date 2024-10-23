// static/script.js
function fetchWeatherData() {
    fetch('/get_weather_data')
        .then(response => response.json())
        .then(data => {
            displayWeatherData(data);
        });
}

function fetchAlerts() {
    fetch('/get_alerts')
        .then(response => response.json())
        .then(alerts => {
            displayAlerts(alerts);
        });
}

function displayWeatherData(data) {
    const summaryContainer = document.getElementById('weather-summary');
    summaryContainer.innerHTML = '';

    for (const [city, summary] of Object.entries(data)) {
        summaryContainer.innerHTML += `
            <div class="weather-summary">
                <h3>${city}</h3>
                <p>Average Temperature: ${summary.average_temp}°C</p>
                <p>Max Temperature: ${summary.max_temp}°C</p>
                <p>Min Temperature: ${summary.min_temp}°C</p>
                <p>Dominant Condition: ${summary.dominant_condition}</p>
            </div>
        `;
    }
}

function displayAlerts(alerts) {
    const alertContainer = document.getElementById('alerts');
    alertContainer.innerHTML = '';

    if (alerts.length === 0) {
        alertContainer.innerHTML = '<p>No alerts at the moment.</p>';
    } else {
        alerts.forEach(alert => {
            alertContainer.innerHTML += `<p>${alert}</p>`;
        });
    }
}

// Call functions to fetch data
fetchWeatherData();
fetchAlerts();
