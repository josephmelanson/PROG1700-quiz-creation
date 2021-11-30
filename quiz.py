import sys


def main():
    if len(sys.argv) < 3:
        sys.exit(-1)
    input_parameter = sys.argv[1]
    input_filename = sys.argv[2]
    if input_parameter == 'create':
        create_quiz(input_filename)
    elif input_parameter == 'run':
        results = run_quiz(input_filename)
        print(results)
    elif input_parameter != 'create' or input_parameter != 'run':
        sys.exit(-1)


def create_sample_quiz(filename):
    questions = [['TF','This is a sample question.','T'], ['MC','This is a sample question.','2','Choice 1','Choice 2','Choice 3','Choice 4']]
    with open(filename,'w') as f:
        for r in questions:
            new_rec = f"{r[0]},{r[1]}\n"
            f.write(new_rec)


def display_truefalse(question, answer):
    question_three = question
    answer_three = input(f"{question_three}\nEnter your answer (T or F): ")
    if answer_three == answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect, the answer is {answer}.")
        return False


def display_multiplechoice(question, answer, choices):
    if len(choices) == 0:
        raise ValueError
    question_four = question
    choices_four = choices
    print(f"Your question is: {question_four}\nYour options are:")
    for i,c in enumerate(choices_four, start=1):
        print(f"{i}) {c}")
    answer_four = input("Enter your answer: ")
    if answer_four == answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect, the answer is {answer}.")
        return False


def display_question(line):
    list_five = line.split(",")
    question_five = list_five[1]
    answer_five = list_five[2]
    choices_five = list_five[3:]
    if list_five[0] == 'TF':
        five_tf_result = display_truefalse(question_five, answer_five)
        return five_tf_result
    elif list_five[0] == 'MC':
        five_mc_result = display_multiplechoice(question_five, answer_five, choices_five)
        return five_mc_result


def run_quiz(filename):
    tally_ans = 0
    tally_ques = 0
    with open(filename) as f:
        for line in f:
            result = display_question(line.strip())
            tally_ques += 1
            if result:
                tally_ans += 1
    tally_totes = (tally_ans / tally_ques) * 100
    tally_final = f"You have {tally_ans}/{tally_ques} ({tally_totes:,.2f}%) correct."
    return tally_final


def create_truefalse():
    tf_question_input = input("Enter a true or false question: ")
    tf_answer_input = input("Enter the correct answer (T/F): ")
    list_seven = ["TF"]
    list_seven.append(tf_question_input)
    list_seven.append(tf_answer_input)
    tf_seven_final = ','.join(list_seven)
    return tf_seven_final


def create_multiplechoice():
    list_eight = ["MC"]
    mc_question_input = input("Enter a multiple choice question: ")
    list_eight.append(mc_question_input)
    mc_choice_input = "."
    while mc_choice_input != '':
        mc_choice_input = input("Enter a possible choice (ENTER to end): ")
        if mc_choice_input != '':
            list_eight.append(mc_choice_input)
    print(f"Your question is: {list_eight[1]}\nYour choices are:")
    for i,c in enumerate(list_eight[2:], start=1):
        print(f"{i}) {c}")
    mc_answer_input = input("Enter the correct answer (number): ")
    list_eight.insert(2,mc_answer_input)
    mc_eight_final = ','.join(list_eight)
    return mc_eight_final


def create_question():
    type_selection = input("Which type of question do you want to create (MC, TF, or ENTER to end)? ")
    type_selection = type_selection.lower()
    if type_selection == "mc":
        output_alpha = create_multiplechoice()
        return output_alpha
    if type_selection == "tf":
        output_beta = create_truefalse()
        return output_beta
    elif type_selection == '':
        return type_selection


def create_quiz(filename):
    f = open(filename, 'w')
    test_loop = create_question()
    while test_loop != '':
        f.write(test_loop + '\n')
        test_loop = create_question()
    print("Quiz created!")
    f.close()


if __name__ == "__main__":
    main()