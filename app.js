document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("mysubmit").onclick = function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        var state = document.getElementById("state").value;
        var wait = document.getElementById("wait").value;
        var date = document.getElementById("Departure_date").value;
        var r_date = document.getElementById("Returning_date").value;

        // Fetch JSON data
        fetch('data.json') // Adjust the URL to your JSON file or API endpoint
            .then(response => response.json())
            .then(data => {
                // Filter the JSON data based on user input
                var filteredData = data.filter(item => {
                    return item.state === state && item.wait === wait && item.date === date && item.r_date === r_date;
                });

                // Update the table with the filtered data
                updateTable(filteredData);
            })
            .catch(error => {
                console.error('Error fetching JSON data:', error);
                // Handle errors if the JSON data cannot be fetched
            });
    };
});

function updateTable(data) {
    var table = document.querySelector("table"); // Select the table element
    var tbody = table.querySelector("tbody"); // Select the table body element

    // Clear existing table rows except for the header row
    tbody.innerHTML = '';

    // Iterate over the filtered data and populate the table rows
    data.forEach(item => {
        var row = tbody.insertRow(); // Insert a new row
        row.insertCell().textContent = item.busNumber; // Populate cell with bus number
        row.insertCell().textContent = item.departure; // Populate cell with departure info
        row.insertCell().textContent = item.duration; // Populate cell with duration
        row.insertCell().textContent = item.arrival; // Populate cell with arrival info
        row.insertCell().textContent = item.fare; // Populate cell with fare
        row.insertCell().textContent = item.seatAvailability; // Populate cell with seat availability

        // Create a button for choosing seat
        var chooseSeatCell = row.insertCell();
        var chooseSeatButton = document.createElement("button");
        chooseSeatButton.textContent = "Choose Seat";
        chooseSeatButton.onclick = function() {
            // Add your logic for choosing a seat here
            console.log("Seat chosen for bus number:", item.busNumber);
        };
        chooseSeatCell.appendChild(chooseSeatButton);
    });
}

       