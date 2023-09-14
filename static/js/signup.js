// button = document.getElementById("signupbtn")
// button.addEventListener('click', console.log("hi"))

form = document.getElementById("signup");
form.addEventListener("submit", function (e) {
  e.preventDefault();
  post_login();
});

async function post_login() {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  console.log(email, password);

  const res = await fetch("http://127.0.0.1:5000/submit-info", {
    method: "POST",
    headers: {
      Accept: "application.json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      mail: email,
      pw: password,
    }),
  });

  const id = await res.json();

  localStorage.setItem("uid", id.uid)
  window.location.replace("grablinks/" + id.uid);
}
