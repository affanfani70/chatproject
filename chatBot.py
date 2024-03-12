from difflib import get_close_matches


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    close_matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if close_matches:
        return close_matches[0]


def chatbot(knowledge: dict) -> None:
    while True:
        user_input = input("You: ")
        best_match = get_best_match(user_input, knowledge)
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: Sorry! I did not understand....')


if __name__ == '__main__':
    brain: dict = {
        'hello': 'Hey! how can i help',
        'how are you': 'I am good. How are you?',
        'what is your name?': 'I am an artificial intelligence Bot just to entertain you',
        'bye': 'Nice to meet you. will see you again'
    }

    chatbot(knowledge=brain)
