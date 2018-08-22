class Player():
    def __init__(self,name,surname,sex,age, party, popularity):
        self.age=age
        self.sex=sex
        self.name = name
        self.surname=surname
class Politycian():
    def __init__(self, name, surname, sex, age, popularity, truthfulness, eloquence, views, corruptibility, education, profession, party):
        self.age=age
        self.sex=sex
        self.name = name
        self.surname=surname
        self.truthfulness=truthfulness
        self.eloquence=eloquence
        self.views=views
        self.corruptibility=corruptibility
        self.education=education
        self.party=party
        self.profession = profession
class Party():
    def __init__(self,name,chairman,views,members,doctrine,description):
        self.name=name
        self.chairman = chairman
        self.views = views
        self.members=[]#list
        self.doctrine=doctrine
        self.description=description

        

