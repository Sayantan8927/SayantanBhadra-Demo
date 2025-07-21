function rollDice() {
  const dice1 = Math.floor(Math.random() * 6) + 1;
  const dice2 = Math.floor(Math.random() * 6) + 1;

  document.getElementById('dice1').src = `https://upload.wikimedia.org/wikipedia/commons/${diceImagePath(dice1)}.png`;
  document.getElementById('dice2').src = `https://upload.wikimedia.org/wikipedia/commons/${diceImagePath(dice2)}.png`;

  let resultText = "";
  if (dice1 > dice2) {
    resultText = "🎉 Player 1 Wins!";
  } else if (dice2 > dice1) {
    resultText = "🎉 Player 2 Wins!";
  } else {
    resultText = "😲 It's a Draw!";
  }

  document.getElementById('result').textContent = resultText;
}

// Map dice number to Wikimedia file path
function diceImagePath(dice) {
  const map = {
    1: "2/2c/Alea_1",
    2: "b/b8/Alea_2",
    3: "2/2f/Alea_3",
    4: "8/8d/Alea_4",
    5: "5/55/Alea_5",
    6: "8/8d/Alea_6"
  };
  return map[dice];
}
