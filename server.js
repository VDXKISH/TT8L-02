const fs = require('fs');

// Read the JSON data from file
fs.readFile('data.json', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading JSON file:', err);
        return;
    }

    try {
        // Parse the JSON data
        const jsonData = JSON.parse(data);

        // Process the data (filtering, etc.)
        const filteredData = jsonData.filter(item => {
            return item.state === state && item.wait === wait && item.date === date && item.r_date === r_date;
        });

        // Update the table (assuming you have the updateTable function defined)
        updateTable(filteredData);
    } catch (err) {
        console.error('Error parsing JSON data:', err);
    }
});

// Define the updateTable function
function updateTable(data) {
    // Your table update logic here
}