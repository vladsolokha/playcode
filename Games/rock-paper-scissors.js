// List of icons that can be used in the game
var icons = ["icon://fa-hand-rock-o", "icon://fa-hand-paper-o", "icon://fa-hand-scissors-o"];

// List of possible choices to play
var choices = ["Rock", "Paper", "Scissors"];

// User and computer scores, started at 0
var playerScore = 0;
var computerScore = 0;

// Button for player to play rock
onEvent("rockButton","click",function(){
  updateScreen("Rock");
});

// Button for player to play paper
onEvent("paperButton","click",function(){
  updateScreen("Paper");
});

// Button for player to play scissors
onEvent("scissorsButton","click",function(){
  updateScreen("Scissors");
});

// When the user clicks any of the three buttons it runs a round
// of rock paper scissors. This function determines who won the
// game and updates the screen and scores for each player.
function updateScreen(playerChoice){
  
  // Randomly choose the computer's choice and decide who wins
  var computerChoice = randomChoose(choices);
  var winner = decideWinner(playerChoice, computerChoice);

  // Update the screen with the correct icon for each player
  setProperty("playerOutput","image",findIcon(playerChoice));
  setProperty("computerOutput","image",findIcon(computerChoice));

  
  // Update the screen with the text explaining who won.
  if(winner == "Draw"){
    setProperty("gameText","text","Draw!");
  } else if (winner == "Player") {
    setProperty("gameText","text","You win!");
    playerScore++;
    setProperty("playerScoreOutput","text",playerScore);
  } else if (winner == "Computer") {
    setProperty("gameText","text","Computer wins!");
    computerScore++;
    setProperty("computerScoreOutput","text",computerScore);    
  }
}

// iconName {string} - either "Rock", "Paper", or "Scissors"
// return {string} - the icon associated with the string provided
function findIcon(iconName){
    if (iconName == "Rock") {
      return icons[0];
    } else if (iconName == "Paper") {
      return icons[1];
    } else {
      return icons[2];
    }
}

// Randomly selects an item from the list provided and returns it
// list {list} - a list of items
// return {string} - a randomly chosen item from the list
function randomChoose(list){
    return list[randomNumber(0,list.length-1)];
}
// Decides who wins a round of rock paper scissors by taking the two 
// playerChoice {string} - either "Rock", "Paper", or "Scissors", the human player's choice
// computerChoice {string} - either "Rock", "Paper", or "Scissors", the computer player's choice
// return {string} - either "Draw", "Player", or "Computer", depending on who 
function decideWinner(playerChoice, computerChoice){
  // If choices match return Draw {string}
  if (playerChoice == computerChoice) {
    return "Draw";
  } else if (
      // Anytime the player wins
      (playerChoice == 'Rock' && computerChoice == 'Scissors') ||
      (playerChoice == 'Paper' && computerChoice == 'Rock') ||
      (playerChoice == 'Scissors' && computerChoice == 'Paper')) {
    return "Player";
  } else {
    return "Computer";
  }
}