const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3033;

// Middleware to parse request bodies
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve static files
app.use(express.static('static'));

// Set seat.html as the first page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'template', 'seat.html'));
});

// Route to handle saving selected seats to a text file
app.post('/saveSeats', (req, res) => {
    const selectedSeats = req.body.selectedSeats;
    console.log('Received seats:', selectedSeats);

    fs.appendFile('selected_seats.txt', JSON.stringify(selectedSeats) + '\n', (err) => {
        if (err) {
            console.error('Failed to save selected seats:', err);
            return res.status(500).send('Failed to save selected seats');
        }
        res.redirect('/passenger_details');
    });
});

// Serve passenger_details.html
app.get('/passenger_details', (req, res) => {
    res.sendFile(path.join(__dirname, 'template', 'passenger_details.html'));
});

app.post('/savePassengerDetails', (req, res) => {
    const passengerDetails = req.body.passengers;

    // Initialize total payment due for all passengers
    let overallTotalAmount = 0;

    // Prepare the data to be saved
    const data = passengerDetails.map(passenger => {
        // Calculate ticket price based on age
        let ticketPrice;
        if (passenger.age >= 4 && passenger.age <= 12) {
            ticketPrice = 12;
        } else if (passenger.age >= 13 && passenger.age <= 59) {
            ticketPrice = 22;
        } else {
            ticketPrice = 0;
        }

        // Calculate total amount based on food orders
        let foodTotalAmount = 0;
        let foodOrder = {};
        for (let foodItem in passenger.food) {
            if (passenger.food[foodItem]) {
                const foodQuantity = passenger.food[foodItem];
                const foodPrice = getPrice(foodItem);
                foodTotalAmount += foodQuantity * foodPrice;
                foodOrder[foodItem] = foodQuantity;
            }
        }

        // Calculate total price including ticket and food
        let totalPrice = ticketPrice + foodTotalAmount;

        // Accumulate to the overall total amount
        overallTotalAmount += totalPrice;

        return `Seat: ${passenger.seat}, Name: ${passenger.name}, Age: ${passenger.age}, Ticket Price: MYR ${ticketPrice}, Food Order: ${JSON.stringify(foodOrder)}, Total Amount: MYR ${totalPrice}\n`;
    }).join('');

    // Save passenger data to the file
    fs.appendFile('selected_seats.txt', data, (err) => {
        if (err) {
            console.error('Failed to save passenger details:', err);
            return res.status(500).send('Failed to save passenger details');
        }
        console.log('Passenger details saved successfully');
        // Send the total amount to be paid as response
        res.status(200).send(`Total Amount to be paid: MYR ${overallTotalAmount}`);
    });
});

function getPrice(foodItem) {
    switch (foodItem) {
        case 'sandwich':
            return 4.50;
        case 'chickenburger':
            return 6.00;
        case '7Days Vanilla Croissant':
            return 1.00;
        case '7Days Chocolate Croissant':
            return 1.00;
        case 'nasilemak':
            return 3.00;
        case 'chickenrice':
            return 3.00;
        default:
            return 0;
    }
}

// Serve payment.html
app.get('/payment', (req, res) => {
    res.sendFile(path.join(__dirname, 'template', 'payment.html'));
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
