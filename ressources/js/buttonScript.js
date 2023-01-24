function coinFlip() {
    let choice ="Your choice is: head";
    let rand =Math.floor(Math.random() * 2);


    if(rand === 1){
        choice = "Your choice is: tail";
    }
    
    document.getElementById("resultText").innerHTML = choice;
}


document.getElementById("coinButton").addEventListener("click", coinFlip);
