const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const app = express();
const port = 3009;

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/submit_form', (req, res) => {
    const { action, name, email, password } = req.body;
    const dataFilePath = path.join(__dirname, 'data.json');

    fs.readFile(dataFilePath, 'utf8', (err, fileData) => {
        if (err) {
            console.error('Error reading file:', err);
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
            fs.writeFile(dataFilePath, JSON.stringify(jsonData, null, 2), (err) => {
                if (err) {
                    console.error('Error writing file:', err);
                    return res.status(500).send('Internal Server Error: Unable to write data file.');
                }

                res.status(200).send({ message: 'Sign-up successful!' });
            });
        } else if (action === 'login') {
            const user = jsonData.find(user => user.email === email && user.password === password);
            if (user) {
                res.status(200).send({ message: 'Log-in successful!' });
            } else {
                res.status(400).send('Invalid email or password.');
            }
        } else {
            res.status(400).send('Invalid action.');
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
