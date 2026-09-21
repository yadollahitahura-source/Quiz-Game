class Question:
        def __init__(
        self,
        text: str,
        options: list[str],
        correct: str
    ) -> None:
            self.__text: str = text
            self.__options: list[str] = options
            self.__correct: str = correct

        def is_correct(self, choice: str) -> bool:
            return choice.strip().upper() == self.__correct

        def correct_text(self) -> str:
            return self.__options["ABCD".index(self.__correct)]


class match:
    def __init__(
        self,
        player1: str,
        player2: str,
        questions: list[Question]
    ) -> None:
        if player1 == player2:
            raise ValueError("Unique Name per Player!")

        self.__players: list[str] = [player1, player2]
        self.__questions: list[Question] = questions
        self.__scores: dict[str, int] = {
            player1: 0,
            player2: 0
        }
        self.__round: int = 0
        self.__answers: dict[str, tuple[str, int]] = {}

    def start_round(self) -> Question:
        self.__round += 1
        self.__answers = {}
        return self.__questions[self.__round - 1]

    def submit(
        self,
        player: str,
        choice: str,
        elapsed: int
    ) -> None:
        self.__answers[player] = (choice, elapsed)

    def resolve_round(self) -> None:
        question: Question = self.__questions[self.__round - 1]

        for player in self.__players:
            choice: str
            elapsed: int

            choice, elapsed = self.__answers[player]

            if elapsed > 30:
                self.__scores[player] += 0

            if question.is_correct(choice):
                self.__scores[player] += 10

    def is_over(self) -> bool:
        return self.__round > 5

    def winner(self) -> str | None:
        player1: str
        player2: str

        player1, player2 = self.__players

        if self.__scores[player1] == self.__scores[player2]:
            return None

        if self.__scores[player1] > self.__scores[player2]:
            return player1
        else:
            return player2