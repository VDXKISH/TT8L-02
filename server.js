const express = require('express');
const fs = require('fs');

const app = express();
const port = 3000;

// Serve HTML page
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Handle form submission
app.get('/submit', (req, res) => {
    // Extract user input from query parameters
    const state = req.query.state;
    const wait = req.query.wait;
    const date = req.query.date;

    // Read and parse JSON data
    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            res.status(500).send('Internal Server Error');
            return;
        }

        try {
            const jsonData = JSON.parse(data);

            // Filter JSON data based on user input
            const filteredData = jsonData.filter(item => {
                return item.state === state && item.wait === wait && item.date === date;
            });

            // Return filtered data as JSON response
            res.json(filteredData);
        } catch (err) {
            console.error('Error parsing JSON data:', err);
            res.status(500).send('Internal Server Error');
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});