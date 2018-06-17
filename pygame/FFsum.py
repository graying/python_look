# python 3 is needed
import random

max_number = 50
count = 1


def generate_number(max_number):
    random.seed()
    return random.randint(1, max_number)


def create_question(num1, num2, operator):
    question_str = str(num1)
    if operator == 1:
        question_str = question_str + '+'
    else:
        question_str = question_str + '-'

    question_str += str(num2)
    return question_str + '='


while True:
    num1 = generate_number(max_number)
    num2 = generate_number(max_number)

    if num1 < num2:
        tmp = num1
        num1 = num2
        num2 = tmp

    # print(num1, num2)
    operator = random.randint(1, 2)
    answer = int(input(str(count) + '.   ' + create_question(num1, num2, operator)))
    count += 1
    if operator == 1:
        calculate = num1 + num2
    else:
        calculate = num1 - num2

    if calculate == int(answer):
        print("Correct!  :)")
    else:
        print("Wrong answer ... :(")
