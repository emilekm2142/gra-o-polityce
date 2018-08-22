# -*- coding: utf-8 -*-
import curses
import time
import pickle
import _thread
import random
        self.ideologieslist=["conservatism","liberalism","nationalism","christian-democracy","social-democracy","comunism","fascism",'Agrarianism',"monarchist"]
        self.partylist=[]
        #wczytywanie parties.xml
        imionameskie = open("imionameskie_UTF-8.txt").read().splitlines()
        imionadamskie = open("imionadamskie_UTF-8.txt").read().splitlines()
        nazwiska = open("nazwiska_UTF-8.txt").read().splitlines()
        self.politycianslist=[]
        for i in range(1000):
            rand=random.randint(1,2)
            if (rand==1):
               imie = random.choice(imionadamskie)
               nazwisko = random.choice(nazwiska)
               sex='female'
            elif (rand==2):
                imie=random.choice(imionameskie)
                nazwisko=random.choice(nazwiska)
                sex='male'

            self.politycianslist.append(Politycian(imie,nazwisko,sex,random.randint(20,70),random.randint(0,100),random.randint(0,100),'',random.choice(self.ideologieslist),random.randint(0,100),random.randint(0,100),random.choice(['wysokie','niskie','srednie']),'',random.choice(self.partylist)))
        #zapisywanie polityków
        with open ('politycy.pickle', 'wb') as fp:
            pickle.dump(self.politycianslist, fp)
        
      
        #wczytywanie polityków
        with open ('politycy.pickle', 'rb') as fp:
            self.politycianslist = pickle.load(fp)
