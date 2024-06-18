const express = require('express');
const fs = require('fs');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

const app = express();
const port = 3006;

let latestBatchId = ''; // Variable to store the latest batch ID

// Middleware to parse URL-encoded data and JSON
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve static files from the 'static' directory
app.use(express.static(path.join(__dirname, 'static')));

// Serve seat selection page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'template', 'seat.html'));
});

// Handle seat selection submission
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

// Serve passenger details page
app.get('/passenger_details', (req, res) => {
    res.sendFile(path.join(__dirname, 'template', 'passenger_details.html'));
});

app.post('/savePassengerDetails', (req, res) => {
    const passengerDetails = req.body.passengers;
    const batchId = uuidv4(); // Unique identifier for this batch of passenger details

    latestBatchId = batchId; // Update the latest batch ID

    let overallTotalAmount = 0;

    const data = passengerDetails.map(passenger => {
        let ticketPrice;
        if (passenger.age >= 4 && passenger.age <= 12) {
            ticketPrice = 12;
        } else if (passenger.age >= 13 && passenger.age <= 59) {
            ticketPrice = 22;
        } else {
            ticketPrice = 0;
        }

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

        let totalPrice = ticketPrice + foodTotalAmount;

        overallTotalAmount += totalPrice;

        return `BatchId: ${batchId}, Seat: ${passenger.seat}, Name: ${passenger.name}, Age: ${passenger.age}, Ticket Price: MYR ${ticketPrice}, Food Order: ${JSON.stringify(foodOrder)}, Total Amount: MYR ${totalPrice}\n`;
    }).join('');

    fs.appendFile('selected_seats.txt', data, (err) => {
        if (err) {
            console.error('Failed to save passenger details:', err);
            return res.status(500).send('Failed to save passenger details');
        }
        console.log('Passenger details saved successfully');
        res.status(200).send(overallTotalAmount.toFixed(2));
    });
});

// Serve payment page
app.get('/payment', (req, res) => {
    res.sendFile(path.join(__dirname, 'template', 'payment.html'));
});

// Handle payment submission
app.post('/payment', (req, res) => {
    // Process payment logic here
    // Assuming validation and processing of payment data

    // Redirect to receipt page after payment processing
    res.redirect('/receipt');
});

app.get('/receipt', (req, res) => {
    fs.readFile('selected_seats.txt', 'utf8', (err, data) => {
        if (err) {
            console.error('Failed to read passenger details:', err);
            return res.status(500).send('Failed to generate invoice');
        }

        const passengers = data.split('\n').filter(line => line.trim() !== '');

        const filteredPassengers = passengers.filter(passenger => passenger.includes(`BatchId: ${latestBatchId}`));

        let overallTotalAmount = 0;
        const receiptRows = filteredPassengers.map(passenger => {
            const details = passenger.split(', ');
            const totalPriceStr = details.find(detail => detail.includes('Total Amount: MYR'));
            const totalPrice = parseFloat(totalPriceStr.split('Total Amount: MYR ')[1]);
            overallTotalAmount += totalPrice;

            return `
                <tr>
                    <td>${details[1].split(': ')[1]}</td>
                    <td>${details[2].split(': ')[1]}</td>
                    <td>${details[3].split(': ')[1]}</td>
                    <td>${details[4].split(': ')[1]}</td>
                    <td>${details[5].split(': ')[1]}</td>
                    <td>${totalPrice.toFixed(2)}</td>
                </tr>
            `;
        }).join('');

        fs.readFile(path.join(__dirname, 'template', 'receipt.html'), 'utf8', (err, template) => {
            if (err) {
                console.error('Failed to read receipt template:', err);
                return res.status(500).send('Failed to generate invoice');
            }

            const receiptHtml = template.replace('<!-- Data rows will be inserted here dynamically -->', receiptRows);
            const finalReceiptHtml = receiptHtml.replace('<span id="totalAmount"></span>', overallTotalAmount.toFixed(2));

            res.send(finalReceiptHtml);
        });
    });
});


// Function to get food price
function getPrice(foodItem) {
    switch (foodItem) {
        case 'sandwich':
            return 4.50;
        case 'chickenburger':
            return 6.00;
        case '7Days Vanilla Croissant':
        case '7Days Chocolate Croissant':
            return 1.00;
        case 'nasilemak':
        case 'chickenrice':
            return 3.00;
        default:
            return 0;
    }
}

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
