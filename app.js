const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3014;

// Serve static files
app.use(express.static('static'));

// Set seat.html as the first page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'template', 'seat.html'));
});

// Middleware to parse request bodies
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Route to handle saving selected seats to a text file
app.post('/saveSeats', (req, res) => {
    let selectedSeats = req.body.selectedSeats;

    // Write selected seat IDs to a text file
    fs.appendFile('selected_seats.txt', JSON.stringify(selectedSeats) + '\n', (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Failed to save selected seats'); // Send an error response
        } else {
            res.status(200).send('Selected seats saved successfully'); // Send a success response
        }
    });
});


app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
