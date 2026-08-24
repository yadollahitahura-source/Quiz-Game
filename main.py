from rich.console import Console
console = Console()

questions: list[tuple[str, list[str], str]] = [
    ("questions1", ["A) 10", "B)20", "C)15", "D)12"], "B"),
    ("questions2", ["A) 12", "B)22", "C)2", "D)11"], "B"),
    ("questions3", ["A) 14", "B)34", "C)3", "D)6"], "B"),
    ("questions4", ["A) 12", "B)16", "C)18", "D)22"], "B"),
    ("questions5", ["A) 8", "B)10", "C)14", "D)16"], "B"),
]

while True:
    print("\n1- شروع بازی")
    print("2- خروج")

    choice = input("انتخاب شما: ")

    if choice == "1":
        score = 1
        correct_count = 0

        for question, options, correct_answer in questions:
            print(f"\n{question}")

            for opt in options:
                print(opt)

            answer: str = input("your answer: ").strip().upper()

            if answer == correct_answer:
                print("correct")
                score += 10
                correct_count += 1
                console.print("correct", style="green")
            else:
                console.print("incorrect", style="red")

        console.print(correct_count / len(questions) * 100)

    elif choice == "2":
        print("خداحافظ")
        break

    else:
        print("انتخاب .نامعتبر است")