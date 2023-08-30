
button = document.getElementById("signupbtn")
button.addEventListener('click', confirm)

function confirm() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    console.log(email,password)
}


