class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


prompts = [
    "What color are apples? \n(a) Red/Green \n(b) Orange: \n",
    "What is the color of the sky? \n(a) Red \n(b) Blue: \n"
]

questions = [
    Question(prompts[0], "a"),
    Question(prompts[1], "b")
]


def run_test(questions):
    score = 0
    for quest in questions:
        answer = input(quest.prompt)
        if answer == quest.answer:
            score += 1
    num_len = len(questions)
    print(f"You got {score} right out of {num_len}")


run_test(questions)
