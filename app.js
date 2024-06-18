const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const port = 3045;

// Middleware to parse JSON and URL-encoded bodies
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Path to store user data
const dataFilePath = path.join(__dirname, 'data.txt');

// Create data file if it doesn't exist
if (!fs.existsSync(dataFilePath)) {
    try {
        fs.writeFileSync(dataFilePath, '[]', 'utf8');
        console.log('Created new data file at:', dataFilePath);
    } catch (err) {
        console.error('Error creating data file:', err);
    }
} else {
    console.log('Data file exists at:', dataFilePath);
}

app.post('/submit_form', (req, res) => {
    const { action, name, email, password } = req.body;

    fs.readFile(dataFilePath, 'utf8', (err, fileData) => {
        if (err) {
            console.error(`Error reading file: ${dataFilePath}`, err);
            return res.status(500).send('Internal Server Error: Unable to read data file.');
        }

        let jsonData = [];
        if (fileData.length > 0) {
            try {
                jsonData = JSON.parse(fileData);
            } catch (parseError) {
                console.error('Error parsing JSON data:', parseError);
                return res.status(500).send('Internal Server Error: Invalid JSON data.');
            }
        }

        if (action === 'signup') {
            const existingUser = jsonData.find(user => user.email === email);
            if (existingUser) {
                return res.status(400).send('User already exists.');
            }

            jsonData.push({ name, email, password });
            fs.writeFile(dataFilePath, JSON.stringify(jsonData), 'utf8', (err) => {
                if (err) {
                    console.error('Error writing file:', err);
                    return res.status(500).send('Internal Server Error: Unable to write data file.');
                }

                res.status(200).send({ message: 'Sign-up successful!' });
            });
        } else if (action === 'login') {
            const user = jsonData.find(user => user.email === email && user.password === password);
            if (user) {
                // Store user info in localStorage for client-side session management
                res.status(200).send({ message: 'Log in successful!', user });
            } else {
                res.status(400).send('Invalid email or password.');
            }
        } else {
            res.status(400).send('Invalid action.');
        }
    });
});



// Handle form submission (Jun's server)
app.get('/submit', (req, res) => {
    const { state, wait, date } = req.query;
    console.log(state, wait, date);

    fs.readFile('bus.txt', 'utf8', (err, data) => {
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
            console.log(filteredData);

            res.json(filteredData);
        } catch (err) {
            console.error('Error parsing JSON data:', err);
            res.status(500).send('Internal Server Error');
        }
    });
});

// Default route to serve frontpage.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'frontpage.html'));
});

// Start server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
