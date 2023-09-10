form = document.getElementById("signup")
form.addEventListener('submit', function(e) {e.preventDefault(); post_login()})
    
async function post_login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    console.log(email, password)

    const res = await fetch("http://localhost:5000/submit-info", {
        method: "POST",
        headers: {
            "Accept": 'application.json',
            "Content-type": "application/json"
        },
        body: JSON.stringify({
            mail:email,
            pw:password
        })
    })

    const id = await res.json()

    window.location.replace("grablinks/"+ id.uid)
}
