// passenger_details.html

let selectedTickets = JSON.parse(sessionStorage.getItem("selectedTickets"));

let passengerInfo = document.querySelector(".passenger-info");

selectedTickets.forEach((ticket, index) => {
  let passengerNum = index + 1;
  passengerInfo.insertAdjacentHTML(
    "beforeend",
    `<div class="passenger">
      <h3>Passenger ${passengerNum}</h3>
      <div class="form-group">
        <label for="name${passengerNum}">Name:</label>
        <input type="text" id="name${passengerNum}" name="name${passengerNum}" required>
      </div>
      <div class="form-group">
        <label for="age${passengerNum}">Age:</label>
        <input type="text" id="age${passengerNum}" name="age${passengerNum}" required>
      </div>
      <div class="form-group">
        <label for="email${passengerNum}">Email:</label>
        <input type="email" id="email${passengerNum}" name="email${passengerNum}" required>
      </div>
      <div class="form-group">
        <label for="phone${passengerNum}">Contact Number:</label>
        <input type="tel" id="phone${passengerNum}" name="phone${passengerNum}" required>
      </div>
    </div>`
  );
})
