function fetch_test(){
    fetch("/ftest").then(response => response.json()).then(function(data){
        document.getElementById("to_change").innerHTML = data["some_text"];
    });
}