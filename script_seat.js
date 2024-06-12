
let seats = document.querySelector(".all-seats");
let rows = 20;
let seatsPerRow = 4; 

for (let row = 1; row <= rows; row++) {
  for (let seat = 0; seat < seatsPerRow / 2; seat++) { 
    let seatLabel = seat === 0 ? "A" : "B";
    let seatId = `${row}${seatLabel}`;
    seats.insertAdjacentHTML(
      "beforeend",
      `<input type="checkbox" name="tickets" id="${seatId}" />
       <label for="${seatId}" class="seat">${seatId}</label>`
    );
  }
  
  seats.insertAdjacentHTML(
    "beforeend",
    `<div class="gap"></div>`
  );
  for (let seat = 0; seat < seatsPerRow / 2; seat++) { 
    let seatLabel = seat === 0 ? "C" : "D";
    let seatId = `${row}${seatLabel}`;
    seats.insertAdjacentHTML(
      "beforeend",
      `<input type="checkbox" name="tickets" id="${seatId}" />
       <label for="${seatId}" class="seat">${seatId}</label>`
    );
  }
}

let tickets = seats.querySelectorAll("input");
let countDisplay = document.querySelector(".count");

tickets.forEach((ticket) => {
  ticket.addEventListener("change", () => {
    let count = parseInt(countDisplay.textContent);
    if (ticket.checked) {
      count += 1;
    } else {
      count -= 1;
    }
    countDisplay.textContent = count;
  });
});

function proceedToPassengerDetails() {
// Redirect to passenger details page
window.location.replace("/template/passenger_details.html");

  
};