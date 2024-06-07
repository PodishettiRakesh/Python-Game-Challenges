def loadData():
    try:
        with open("questions.txt", "r")as f:
            data=f.read()
    except FileNotFoundError:
        print(f"error: file not found")
    return data
# print(loadData())


def parseQuestions(data):
    questions=data.split("\n")
    all_Questions=[]
    for question in questions:
        question=question.split(":")
        if len(question)!=5:
            print("skipping in valid question foramt")
            continue
        # print(question)
        dic={}
        dic["question_text"]=question[0]
        dic["choices"]=question[1].split(",")
        dic["correct_option"]=question[2]
        dic["max_marks"]=question[3]
        dic["penality"]=question[4]
        all_Questions.append(dic)
    return all_Questions
# data=loadData()
# print(parseQuestions(data))

def startQuiz(questions):
    for question in questions:
        print("\n"+ question["question_text"])
        choices=question["choices"]
        for i in choices:
            print(i,end=" ")
        print()
        while True:
            try:
                userChoice=int(input("please enter your choice: "))
                if 1<=userChoice<=len(choices):
                    break
                else:
                    print("Invalid option number, please try again later")
            except ValueError:
                print("please enter valid number!")
        question["userChoice"]=userChoice
        if str(userChoice)==question["correct_option"]:
            question["score"]=question["max_marks"]
        else:
            question["score"]=question["penality"]
    return questions
    
# data=loadData()
# questions=parseQuestions(data)
# print(startQuiz(questions))

def scoreReport(questions):
    total_score=0
    for question in questions:
        if question["userChoice"]==question["correct_option"]:
            score=int(question["score"])
            print(f"correct answer! Markes awarded {score}")
            total_score+=score
        else:
            score=int(question["score"])
            print(f"wrong answer! Penality score: {score}")
            total_score+=score
    print(f"your total score is: {total_score}")
# data=loadData()
# questions=parseQuestions(data)
# questions=startQuiz(questions)
# scoreReport(questions)

def runQuiz():
    data=loadData()
    questions=parseQuestions(data)
    questions=startQuiz(questions)
    scoreReport(questions)
runQuiz()