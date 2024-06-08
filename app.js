document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("mysubmit").onclick = function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        var state = document.getElementById("state").value;
        var wait = document.getElementById("wait").value;
        var date = document.getElementById("Departure_date").value;
        var r_date = document.getElementById("Returning_date").value;

        
        fetch('data.json') 
            .then(response => response.json())
            .then(data => {
                
                var filteredData = data.filter(item => {
                    return item.state === state && item.wait === wait && item.date === date && item.r_date === r_date;
                });

                
                updateTable(filteredData);
            })
            .catch(error => {
                console.error('Error fetching JSON data:', error);
            });
    };
});

function updateTable(data) {
    var table = document.querySelector("table"); 
    var tbody = table.querySelector("tbody"); 

    
    tbody.innerHTML = '';

    data.forEach(item => {
        var row = tbody.insertRow(); 
        row.insertCell().textContent = item.busNumber; 
        row.insertCell().textContent = item.departure; 
        row.insertCell().textContent = item.duration; 
        row.insertCell().textContent = item.arrival; 
        row.insertCell().textContent = item.fare; 
        row.insertCell().textContent = item.seatAvailability; 

        
        var chooseSeatCell = row.insertCell();
        var chooseSeatButton = document.createElement("button");
        chooseSeatButton.textContent = "Choose Seat";
        chooseSeatButton.onclick = function() {
            
            console.log("Seat chosen for bus number:", item.busNumber);
        };
        chooseSeatCell.appendChild(chooseSeatButton);
    });
}

       