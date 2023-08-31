function searched(){
    const searchform = document.getElementById('searchform');
    const searchbar = document.getElementById('searchbar').value;
    
    console.log(searchform, searchbar)
}


searchform.addEventListener('submit', searched);
