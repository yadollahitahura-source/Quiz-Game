import json
import random

from engine import Question,ROUNDS

QUESTION_PATH="question.json"

class QuestinBank:
    def __init__(self,path:str=QUESTION_PATH)->None:
        with open(path,"r",encoding="utf-8")as f:
            data:Any=json.load(f)
        self._qustions:list[Question]=[]
        for item in data:
            Question:Question=Question(
                text=item["question"],
                options=item["options"],
                correct=item["correct"]
            )

            self._qustions.append()
    def count(self)->int:
        pass
    def pick(self,n:int=ROUNDS)->list(Question):
        pass