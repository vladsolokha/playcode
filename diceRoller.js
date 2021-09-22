
function rollingDice() {
    //get random number
    const randNumber = () => {
        let randomNumber = Math.ceil(Math.random() * 10);
        return randomNumber;
    }
    // get element 'die' from HTML assign it to the die;
    const die = document.getElementById('die');
    die = randNumber;
    
    die.innerHTML = die;
}
