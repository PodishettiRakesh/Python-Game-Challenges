def loadData():
    f=open("questions.txt","r")
    data=f.read()
    return data
# print(loadData())

def parseQuestions(data):
    questions=data.split("\n")
    all_Questions=[]
    for question in questions:
        question=question.split(":")
        print(question)
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

