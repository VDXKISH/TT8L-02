const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const port = 3037; 

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(express.static(path.join(__dirname, 'public')));

const dataFilePath = path.join(__dirname, 'data.txt');

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
                res.status(200).send({ message: 'Log in successful!', user });
            } else {
                res.status(400).send('Invalid email or password.');
            }
        } else {
            res.status(400).send('Invalid action.');
        }
    });
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'frontpage.html'));
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
