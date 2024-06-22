const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'bus.html'));
});

// Handle form submission
app.get('/submit', (req, res) => {
    const state = req.query.state;
    const wait = req.query.wait;
    const date = req.query.date;
    console.log(state)
    console.log(wait)
    console.log(date)

    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            res.status(500).send('Internal Server Error');
            return;
        }

        try {
            const jsonData = JSON.parse(data);

            // Filter JSON data based on user input
            const filteredData = jsonData.filter(data => {
                return data.state === state && data.wait === wait && data.date === date;
            });
            console.log(filteredData)

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

