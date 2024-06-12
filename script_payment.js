// payment.html
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