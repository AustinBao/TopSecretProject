
document.addEventListener("submit", function (e) {
    e.preventDefault();
    postDelete();
  });

async function postDelete() {
    var sender = document.getElementById("sender").value;
    var id = document.getElementById("id").value;

    const res = await fetch("http://127.0.0.1:5000/delete-post", {
    method: "POST",
    headers: {
      Accept: "application.json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      usender: sender,
      uid: id,
    }),
  });

  const successfulDelete = await res.json();
  console.log(successfulDelete)

}
