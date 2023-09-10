const currentUrl = window.location.href;
console.log(currentUrl);


fetch(currentUrl)
  .then(res => res.json())
  .then(data => console.log(data)) 