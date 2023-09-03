
fetch("http://localhost:5000/grablinks/26ef0160193549f781c06f483358e1d7")
  .then(res => res.json())
  .then(data => console.log(data)) 