from engine import Question, match

questions = [
    Question(
        "questions1",
        ["A) 10", "B) 20", "C) 15", "D) 12"],
        "B"
    ),

    Question(
        "questions2",
        ["A) 12", "B) 22", "C) 2", "D) 11"],
        "B"
    ),

    Question(
        "questions3",
        ["A) 14", "B) 34", "C) 3", "D) 6"],
        "B"
    ),

    Question(
        "questions4",
        ["A) 12", "B) 16", "C) 18", "D) 22"],
        "B"
    ),

    Question(
        "questions5",
        ["A) 8", "B) 10", "C) 14", "D) 16"],
        "B"
    )
]


print("===== TWO PLAYER QUIZ GAME =====")

player1 = input("Enter player 1 name: ").strip()
player2 = input("Enter player 2 name: ").strip()

while player1 == player2:
    print("Players must have different names!")
    player2 = input("Enter player 2 name: ").strip()


game = match(player1, player2, questions)


while game.round < len(questions):

    question = game.start_round()

    print(f"\n===== Round {game.round} =====")
    print(question.text)

    for option in question.options:
        print(option)

    print(f"\n{player1}'s turn")
    choice1 = input("Your answer: ").strip().upper()

    print(f"\n{player2}'s turn")
    choice2 = input("Your answer: ").strip().upper()

    game.submit(player1, choice1, 0)
    game.submit(player2, choice2, 0)

    game.resolve_round()

    print("\n----- Scores -----")
    print(f"{player1}: {game.scores[player1]}")
    print(f"{player2}: {game.scores[player2]}")


print("\n===== GAME OVER =====")

print(f"{player1}: {game.scores[player1]}")
print(f"{player2}: {game.scores[player2]}")

winner = game.winner()

if winner is None:
    print("It's a draw!")
else:
    print(f"Winner: {winner}")