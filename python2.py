import time

time_limit = 10

questions = {
    "Every rational number is a ? ": "Real number",
    "What is 24 + 18? ": "42",
}


score = 0
st = time.time()


for question, answer in questions.items():

    useranswer = input(question)


    if useranswer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")


    times = time.time() - st
    if times >= time_limit:
        print("Time's up!")
        print('Time management is very important , learn that and do this quiz :(')
        break


print("You scored :-", score, "out of", len(questions))
print("Time spent by you is :", int(times), "seconds")


#Dictionary can be used to enter a group of questions and can be used to simplify the code.
