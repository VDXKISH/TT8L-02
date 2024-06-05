from flask import Flask, request, render_template_string, redirect, url_for


app = Flask(__name__)

passenger_details= '''

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Passenger Details</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    text-align: center;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    font-weight: bold;
}

input[type="text"], input[type="email"], input[type="tel"], select, input[type="number"] {
    width: calc(100% - 20px);
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
}

.submit-btn {
    width: 100%;
    padding: 10px;
    background-color: #000000;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.submit-btn:hover {
    background-color: #000000;
}
</style>
</head>
<body>
<div class="container">
    <h2>Passenger Details</h2>
    <form action="payment.html" method="post">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div class="form-group">
            <label for="age">Age:</label>
            <input type="text" id="age" name="age" required>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="phone">Contact Number:</label>
            <input type="tel" id="phone" name="phone" required>
        </div>

<div class="food-section">
    <h3>Order Food (optional)</h3>
    <table>
      <thead>
        <tr>
          <th>Food</th>
          <th>Price</th>
          <th>Quantity</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Sandwich</td>
          <td>MYR4.50</td>
          <td><input type="number" name="sandwich_quantity" min="0" max="20"></td>
        </tr>
        <tr>
          <td>Chicken Burger</td>
          <td>MYR6.00</td>
          <td><input type="number" name="chickenburger_quantity" min="0" max="20"></td>
        </tr>
        <tr>
          <td>7Days Vanilla Croissant</td>
          <td>MYR1.00</td>
          <td><input type="number" name="7DaysVanillaCroissant_quantity" min="0" max="30"></td>
        </tr>
        <tr>
          <td>7Days Chocolate Croissant</td>
          <td>MYR1.00</td>
          <td><input type="number" name="7DaysChcocalateCroissant_quantity" min="0" max="30"></td>
        </tr>
        <tr>
          <td>Nasi Lemak</td>
          <td>MYR3.00</td>
          <td><input type="number" name="nasilemak_quantity" min="0" max="20"></td>
        </tr>
        <tr>
          <td>Chicken Rice</td>
          <td>MYR3.00</td>
          <td><input type="number" name="chickenrice_quantity" min="0" max="20"></td>
        </tr>
      </tbody>
    </table>
  </div>  

      <input type="submit" class="submit-btn" value="Proceed to Pay">
    </form>
  </div>

  <script>
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
    });
  </script>
</body>
</html>
'''

seat= '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bus Seat Booking</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    body {
    width: 100%;
    height: 100vh;
    margin: 0;
    padding: 0;
  }
  .center {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(to right, rgb(162, 216, 162), rgb(102, 194, 102));
  }
  .tickets {
    width: 550px;
    height: fit-content;
    border: 0.4mm solid rgba(0, 0, 0, 0.08);
    border-radius: 3mm;
    box-sizing: border-box;
    padding: 10px;
    font-family: poppins;
    max-height: 96vh;
    overflow: auto;
    background: white;
    box-shadow: 0px 25px 50px -12px rgba(0, 0, 0, 0.25);
  }
  .ticket-selector {
    background: rgb(243, 243, 243);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: column;
    box-sizing: border-box;
    padding: 20px;
  }
  .head {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 30px;
  }
  .title {
    font-size: 16px;
    font-weight: 600;
  }
  .seats {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    min-height: 150px;
    position: relative;
  }
  .status {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
  }
  .item {
    font-size: 12px;
    position: relative;
  }
  .item::before {
    content: "";
    position: absolute;
    top: 50%;
    left: -12px;
    transform: translate(0, -50%);
    width: 10px;
    height: 10px;
    background: rgb(255, 255, 255);
    outline: 0.2mm solid rgb(120, 120, 120);
    border-radius: 0.3mm;
  }
  .item:nth-child(2)::before {
    background: rgb(180, 180, 180);
    outline: none;
  }
  .item:nth-child(3)::before {
    background: rgb(28, 185, 120);
    outline: none;
  }
  .all-seats {
    display: grid;
    grid-template-columns: repeat(2, 1fr) 60px repeat(2, 1fr);
    grid-gap: 15px;
    margin: 60px 0;
    margin-top: 20px;
    position: relative;
  }
  .seat {
    width: 30px;
    height: 30px;
    background: white;
    border-radius: 0.5mm;
    outline: 0.3mm solid rgb(180, 180, 180);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
  }
  .all-seats input:checked + label {
    background: rgb(28, 185, 120);
    outline: none;
  }
  .seat.booked {
    background: rgb(180, 180, 180);
    outline: none;
  }
  input {
    display: none;
  }
  .price {
    width: 100%;
    box-sizing: border-box;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .total {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    font-size: 16px;
    font-weight: 500;
  }
  .total span {
    font-size: 11px;
    font-weight: 400;
  }
  .price button {
    background: rgb(60, 60, 60);
    color: white;
    font-family: poppins;
    font-size: 14px;
    padding: 7px 14px;
    border-radius: 2mm;
    outline: none;
    border: none;
    cursor: pointer;
  }
  
  </style>
</head>
<body>
  <div class="center">
    <div class="tickets">
      <div class="ticket-selector">
        <div class="head">
          <div class="title">Bus Seat Booking</div>
        </div>
        <div class="seats">
          <div class="status">
            <div class="item">Available</div>
            <div class="item">Booked</div>
            <div class="item">Selected</div>
          </div>
          <div class="all-seats"></div>
        </div>
      </div>
      <div class="price">
        <div class="total">
          <span> <span class="count">0</span> Seats Selected</span>
        </div>
        <button id="proceedBtn" type="button">Proceed to Book</button>
      </div>
    </div>
  </div>
  <script>
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

    
    document.getElementById("proceedBtn").addEventListener("click", function() {
      window.location.href = "C:\\Users\\hp\\OneDrive\\Desktop\\My Project\\TT8L-02\\template\\passenger details.html";
    });      
  </script>
</body>
</html>
'''
payment= '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Gateway</title>
   <style>
    * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
}

.container {
    background-color: white;
    border: 1px solid #ccc;
    width: 60%;
    margin: 40px auto;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    background-color: #333;
    color: white;
    opacity: 0.9;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 30px;
}

.mainhead {
    font-size: 35px;
}

input,
select {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}

input:focus,
select:focus {
    border-color: #666;
}

label {
    font-size: 18px;
    margin-bottom: 5px;
    display: block;
}

.payment-methods {
    display: flex;
    justify-content: space-between;
}

.payment-methods label {
    display: flex;
    align-items: center;
    font-size: 16px;
}

.payment-methods input {
    margin-right: 10px;
}

#creditCardFields,
#walletFields,
#fpxFields {
    display: none;
}

.submit-reset {
    display: flex;
    justify-content: space-between;
}

.submit-reset input {
    width: 48%;
    background-color: #333;
    color: white;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.submit-reset input:hover {
    background-color: #555;
}
</style>
    <script>
        function clearCreditCardFields() {
            document.getElementById("cardNumber_id").value = "";
            document.getElementById("cvvPass_id").value = "";
            document.getElementById("exDate_id").value = "";
        }
    
        function validate() {
            var paymentMethod = document.querySelector('input[name="paymentMethod"]:checked').value;
            
            if (paymentMethod === "creditCard" || paymentMethod === "debitCard") {
                var cardNumber = document.getElementById("cardNumber_id").value;
                var cvv = document.getElementById("cvvPass_id").value;
    
                if (isNaN(cardNumber) || cardNumber.length !== 16) {
                    alert("Please enter a valid 16-digit card number.");
                    return false;
                }
                if (isNaN(cvv) || cvv.length !== 3) {
                    alert("Please enter a valid 3-digit CVV.");
                    return false;
                }
            }
    
            var expiryDate = document.getElementById("exDate_id").value;
    
            var currentDate = new Date();
            var inputDate = new Date(expiryDate);
            if (inputDate < currentDate) {
                alert("Please enter a valid future card expiry date.");
                return false;
            }
    
            return true;
        }
    
        function showPaymentFields() {
            var paymentMethod = document.querySelector('input[name="paymentMethod"]:checked').value;
            var creditCardFields = document.getElementById("creditCardFields");
            var walletFields = document.getElementById("walletFields");
            var fpxFields = document.getElementById("fpxFields");
    
            if (paymentMethod === "creditCard" || paymentMethod === "debitCard") {
                creditCardFields.style.display = "block";
            } else {
                creditCardFields.style.display = "none";
                clearCreditCardFields(); 
            }
    
            walletFields.style.display = paymentMethod === "wallet" ? "block" : "none";
            fpxFields.style.display = paymentMethod === "fpx" ? "block" : "none";
        }
    
        document.getElementById("creditCard").addEventListener("change", function() {
            clearCreditCardFields();
        });
        document.getElementById("debitCard").addEventListener("change", function() {
            clearCreditCardFields();
        });
    </script>      
</head>

<body>

    <div>
        <h2 class="mainhead"><b><u>Payment Form</u></b></h2>

        <div class="container">
            <form action="ticket_page.php" autocomplete="off" method="post" onsubmit="return validate()">
                <h3>Payment Info</h3>
                <div class="payment-methods">
                    <label><input type="radio" name="paymentMethod" value="creditCard" onclick="showPaymentFields()" required> Credit Card</label>
                    <label><input type="radio" name="paymentMethod" value="debitCard" onclick="showPaymentFields()"> Debit Card</label>
                    <label><input type="radio" name="paymentMethod" value="wallet" onclick="showPaymentFields()"> Wallet</label>
                    <label><input type="radio" name="paymentMethod" value="fpx" onclick="showPaymentFields()"> Malaysia Online Bank Transfer (FPX)</label>
                </div>
                <br>
                <div id="creditCardFields">
                    <label for="cardNumber_id">Card Number:</label>
                    <input type="text" name="cardNumber_name" id="cardNumber_id" placeholder="1111222233334444" minlength="16" maxlength="16">
                    <label for="exDate_id">Expiry Date:</label>
                    <input type="date" name="exDate_name" id="exDate_id">
                    <label for="cvvPass_id">CVV:</label>
                    <input type="password" name="cvvPass_name" id="cvvPass_id" placeholder="123" minlength="3" maxlength="3">
                    <label><input type="checkbox" name="saveCard" value="yes"> Save your card for future purchases</label>
                </div>
                <div id="walletFields">
                    <label for="walletProvider">Wallet Provider:</label>
                    <select name="walletProvider" id="walletProvider">
                        <option value="">--Select Wallet--</option>
                        <option value="PayPal">PayPal</option>
                        <option value="GooglePay">Google Pay</option>
                        <option value="ApplePay">Apple Pay</option>
                        <option value="TouchNGo">Touch 'n Go</option>
                        <option value="GrabPay">GrabPay</option>
                    </select>
                </div>
                <div id="fpxFields">
                    <label for="fpxBank">Bank:</label>
                    <select name="fpxBank" id="fpxBank">
                        <option value="">--Select Bank--</option>
                        <option value="Maybank">Maybank</option>
                        <option value="CIMB Bank">CIMB Bank</option>
                        <option value="Public Bank">Public Bank</option>
                        <option value="RHB Bank">RHB Bank</option>
                        <option value="Hong Leong Bank">Hong Leong Bank</option>
                        <option value="AmBank">AmBank</option>
                        <option value="UOB Malaysia">UOB Malaysia</option>
                        <option value="Bank Islam">Bank Islam</option>
                        <option value="OCBC Bank">OCBC Bank</option>
                        <option value="HSBC Bank Malaysia">HSBC Bank Malaysia</option>
                        <option value="Bank Rakyat">Bank Rakyat</option>
                        <option value="Affin Bank">Affin Bank</option>
                        <option value="Alliance Bank">Alliance Bank</option>
                        <option value="Standard Chartered Bank">Standard Chartered Bank</option>
                    </select>
                </div>
                <br>
                <div class="submit-reset">
                    <input type="submit" value="Pay Now">
                    <input type="reset" value="Reset">
                </div>
            </form>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(seat)

@app.route('/passenger_details', methods=['POST'])
def passenger_details():
    selected_seats = request.form.getlist('selected_seats')
    return render_template_string(passenger_details, selected_seats=selected_seats)

@app.route('/payment', methods=['POST'])
def payment():
    passenger_data = request.form
    return render_template_string(payment, passenger_data=passenger_data)


if __name__ == '__main__':
    app.run(debug=True , )


