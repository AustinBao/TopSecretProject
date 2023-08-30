
button = document.getElementById("signupbtn")
button.addEventListener('click', write_user_info_to_txt)

function write_user_info_to_txt() {
    const fs = require("fs");
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    const user_info = [email, password];

    fs.writeFile("./test.txt", email, (err) => {
        if (err) {
            console.error(err);
        return;
          }
        });
        console.log("Data has been Written");
}
