import random
from datetime import datetime
import json
import random as rand
import pandas as pd

class Exam:
    num_Questions = 60
    def __init__(self, user_ID, num_Questions = None):
        self.user_ID = user_ID
        if num_Questions is not None:
            if num_Questions >= 40:
                self.num_Questions = num_Questions
            else:
                num_Questions = 40
                print("Number of questions must be at least 40")
        self.id = str(hash(user_ID + str(datetime.now())))
        self.question_pool = self.load_questions()
        self.subtopics = self.load_subtopics()

    def load_questions(self):
        with open('questions.json') as json_file:
            data = json.load(json_file)
        return data

    def load_subtopics(self):
        with open('topics.json') as json_file:
            data = json.load(json_file)
        return data

    def create_exam(self, id, num_Questions):
        newExam = {}
        topic_list = []

        for topic in self.subtopics:
            for x in range(self.subtopics[topic]["weight"]):
                topic_list.append(topic)
        #print(topic_list)

        for x in range(num_Questions):
            current_topic = random.choice(topic_list)
            #newExam[x] = {element for element in self.question_pool.values() if element['subtopic'] == current_topic}
            #print(newExam[x])

    def getID(self):
        return self.id

    def get_num_questions(self):
        return self.num_Questions

    def get_question_pool(self):
        return self.question_pool

    def get_subtopics(self):
        return self.subtopics


exam = Exam('jesse', 10)
#print(exam.get_question_pool()["2.3_MCQ_10"])
total_weight = 0
for subtopic in exam.get_subtopics():
    total_weight += exam.get_subtopics()[subtopic]["weight"]
#print(total_weight)
#print(exam.get_subtopics())

df = pd.DataFrame.from_dict(exam.question_pool, orient='index')
print(df[df['subtopic'] == '1.1'])
def fun(variable):
    letters = "1.1"
    if (variable == letters):
        return True
    else:
        return False
questions = list(exam.question_pool.values())
sub_questions = filter(fun, questions)
for s in sub_questions:
    print(s)
exam.create_exam(exam.getID(),exam.get_num_questions())