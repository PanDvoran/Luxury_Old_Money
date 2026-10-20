def correct_sentence(text):
    text = text.capitalize()

    if text[-1] != ".":
        text = text + "."

    return text

print(correct_sentence("greetings, friends"))