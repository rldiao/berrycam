
var userScore = 0
var computerScore = 0
const userScore_span = document.getElementById("user-score")
const computerScore_span = document.getElementById("computer-score")
const scoreBoard_div = document.querySelector(".score-board")
const result_p = document.querySelector(".result > p")
const rock_div = document.getElementById("r")
const paper_div = document.getElementById("p")
const scissors_div = document.getElementById("s")

const timeout = 300;

// querySelector is used in this case to get the class
// getElementById is of course by ID

function getComputerMove() {
    const moves = ["r", "p", "s"]
    return moves[Math.floor(Math.random() * 3)]
}

function convertToWord(letter) {
    var output
    switch(letter) {
        case "r":
            output = "Rock"
            break
        case "s":
            output = "Scissors"
            break
        case "p":
            output = "Paper"
            break
    }
    return output
}

function win(userMove, computerMove) {
    const userMove_div = document.getElementById(userMove)
    userScore++
    userScore_span.innerHTML = userScore;
    result_p.innerHTML = `${convertToWord(userMove)} beats ${convertToWord(computerMove)}. You WIN!`
    userMove_div.classList.add("green-glow")
    setTimeout(() => {
        userMove_div.classList.remove("green-glow")
    }, timeout);
}

function lose(userMove, computerMove) {
    userMove_div = document.getElementById(userMove)
    computerScore++
    computerScore_span.innerHTML = computerScore;
    result_p.innerHTML = `${convertToWord(userMove)} loses to ${convertToWord(computerMove)}. You LOSE!`
    userMove_div.classList.add("red-glow")
    setTimeout(() => {
        userMove_div.classList.remove("red-glow")
    }, timeout);
}

function draw(userMove, computerMove) {
    userMove_div = document.getElementById(userMove)
    result_p.innerHTML = "It's a DRAW"
    userMove_div.classList.add("grey-glow")
    setTimeout(() => {
        userMove_div.classList.remove("grey-glow")
    }, timeout);
}

function game(userMove) {
    computerMove = getComputerMove()
    switch(userMove + computerMove) {
        case "rs":
        case "pr":
        case "sp":
            win(userMove, computerMove)
            break
        case "sr":
        case "rp":
        case "ps":
            lose(userMove, computerMove)
            break
        default:
            draw(userMove, computerMove)
    }
}

function main() {
    rock_div.addEventListener('click', () => game("r"))

    paper_div.addEventListener('click', () => game("p"))

    scissors_div.addEventListener('click', () => game("s"))
}
// RUN MAIN
main()