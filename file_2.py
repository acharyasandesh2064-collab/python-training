def ask_question(question):
    answer = input(question + " ")
    return answer
name = ask_question("What is your name?")
print("Hello, " , name)