# -*- coding: utf-8 -*-
import curses
import time
import pickle
import _thread
import random
class Game():
    def __init__(self):
        self.ms=curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.noecho()
        curses.cbreak()
        self.ms.keypad(1)
        self.ms.refresh()
        self.up_screen = curses.newwin(3, 78, 1, 1)
        self.down_screen = curses.newwin(15, 78, 5, 1)
        self.ms.addstr(0,4,"Symulator polityczny",curses.color_pair(1))
    def drawMainMenu(self):
        
        self.up_screen.clear()
        self.down_screen.clear()
        self.up_screen.addstr(1,1,"tekst23")
        self.up_screen.addstr(2,1,"-----------")
        self.down_screen.addstr(1,1,"A:  Nowa Gra")
        self.up_screen.border(0)
        self.down_screen.border(0)
        self.up_screen.refresh()
        self.down_screen.refresh()
        self.ms.refresh()
        while True:
         key = self.ms.getch()
         if (key==ord("A")):  
            
            self.drawCharacterCreating()
         elif (key==ord("q")):
             break;
    def drawCharacterCreating(self):
        self.clear()
        self.up_screen.addstr(1,1,"Tworzenie postaci", curses.A_BOLD)
        self.down_screen.addstr(1,1,"No to róbta swoją postać. Nacisnij jakikolwiek klawisz, aby kontynuować.")
        curses.echo()
        self.refresh()
        self.ms.getch()
        self.down_screen.addstr(5,1,"Imię:", curses.color_pair(2))
        name=self.down_screen.getstr(5,7, 10)
        self.down_screen.addstr(6,1,"Nazwisko:", curses.color_pair(2))
        surname=self.down_screen.getstr(6,10, 20)
        self.down_screen.addstr(7,1,"Wiek:", curses.color_pair(2))
        self.down_screen.addstr(7,10,"TIP: używaj 'p' aby dodać a  'm' aby odjąć. 'o' żeby zatwierdzić", curses.color_pair(1))
        self.refresh()
        curses.noecho()
        age=20
        while True:
            key = self.ms.getch()
            if (key==ord("p")):
                age=age+1
            if (age>=11):
             if (key==ord("m")):
                age=age-1
             elif (key==ord("o")):
                break
           
            self.down_screen.addstr(7,6,str(age), curses.A_BOLD)
            self.refresh()
        self.down_screen.addstr(9,1,"Wybierz płeć: \n a:Mężczyzna\n b:Kobieta", curses.color_pair(2))
        self.refresh()
        while True:

          key = self.ms.getch()
          if (key==ord("a")):
             sex="male"
             self.down_screen.addstr(12,2,"Male", curses.color_pair(1))
             self.refresh()
             break
          elif (key==ord("b")):
             sex="female"
             self.down_screen.addstr(12,2,"Female", curses.color_pair(1))
             self.refresh()
             break
        name = name.decode('UTF-8')
        surname = surname.decode('UTF-8')
        self.player = Player(name,surname,sex,age,'', 0)
        self.down_screen.addstr(13,5,"Your Character has been created! Press any key for continue.", curses.A_BOLD)
        self.refresh()
        self.ms.getch()
        self.drawWorldCreating()
    def drawWorldCreating(self):
        self.clear()
        self.up_screen.addstr(1,1,"Generowanie świata...")
        self.down_screen.addstr(1,1,"To może zając kilka sekund.")
        self.down_screen.addstr(2,1,"Generowanie partii")
        self.refresh()
        self.ideologieslist=["conservatism","liberalism","nationalism","christian_democrats","social_democracy","comunism","fascism",'Agrarianism',"monarchist"]
        self.partylist=[]
        #self,name,chairman,views (list),members,doctrine,desc
		#Komentarz po latach - o panie te opisy od taty xd
		
		
        SLD=Party("Sojusz lewicy demokratycznej",'',["social_democracy"],'','left',"SLD to była partia komunistyczna (PZPR), ostatnim hasłem było 'sztandar wyptowadzić'. Mieli ogromne szanse, ale je zaprzepaszcili. Pierwszym premeierem w nowej formule był Leszek Miller, w starej Mieczysław Rakowski.")
        PIS=Party("Prawo i Sprawiedliwość",'',["conservatism","christian_democrats"],'','right','Prawo i Sprawiedliwość (PiS) – polska konserwatywna partia polityczna zarejestrowana sądownie 13 czerwca 2001 (pierwszy komitet lokalny PiS powstał już 22 marca 2001)[2], założona przez braci Lecha Kaczyńskiego i Jarosława Kaczyńskiego na fali popularności uzyskanej przez Lecha podczas sprawowania przez niego funkcji ministra sprawiedliwości i prokuratora generalnego w rządzie AWS. Deklarowana ideologia partii stanowi połączenie konserwatyzmu, chrześcijańskiej demokracji i wartości republikańskich')
        PO=Party("Platforma Obywatelska",'',['liberalism',"christian_democrats"],'','center','Platforma Obywatelska (PO) – polska partia polityczna założona jako stowarzyszenie 24 stycznia 2001 (pod nazwą "Platforma Obywatelska Rzeczypospolitej Polskiej" zarejestrowana 5 marca 2002)[5]. Jej głównymi założycielami byli Andrzej Olechowski, Maciej Płażyński z AWS i Donald Tusk z Unii Wolności. Skupia osoby o różnych poglądach, głównie konserwatywno-liberalnych i chrześcijańsko-demokratycznych, centroprawicowych i centrowych, określa się jako Nowe Centrum.')
        PRM=Party("Polski ruch monarchistyczny",'',['monarchy'],'','right','30 sierpnia 1991 została zarejestrowana partia Polski Ruch Monarchistyczny, której założycielem, przywódcą i regentem jest Leszek Wierzchowski. Ugrupowanie działa zarówno na terenie Polski, jak i w środowiskach polonijnych w różnych krajach. Liczy ponad 1000 członków. Jego siedziba mieści się w Katowicach (wcześniej znajdowała się w Sosnowcu). Hasłem partii jest "Bóg-Król-Honor-Ojczyzna".')
        KPP=Party("Komunistyczna partia polski",'',['comunism'],'','left','Komunistyczna Partia Polski (KPP, Kompol) – partia polityczna założona w lipcu 2002 (zarejestrowana 9 października 2002). Partia uważa się za historyczną i ideową spadkobierczynię Komunistycznej Partii Polski, działającej w latach 1918–1938[1] oraz SDKPiL. Biuletynem partii jest miesięcznik „Brzask”. Aktualnym przewodniczącym wybranym na III zjeździe partii w grudniu 2010 jest inżynier Krzysztof Szwej, który zastąpił na tym stanowisku płk. dr. Józefa Łachuta.')
        PSL=Party("Polskie Stronnictwo Ludowe",'',['christian_democrats','Agrarianism'],'','center','Polskie Stronnictwo Ludowe (PSL) – centrowa partia agrarystyczna, powstała 5 maja 1990 z połączenia PSL – Odrodzenie (będącego kontynuacją ZSL) oraz wilanowskiego PSL.')
        PJN=Party("polska jest najważniejsza",'',['christian_democrats','liberalism'],'','center','Polska Jest Najważniejsza (PJN) – polska centroprawicowa partia polityczna założona 12 grudnia 2010, zarejestrowana 17 marca 2011. Posiadała klub parlamentarny (w Sejmie VI kadencji i Senacie VII kadencji), obecnie posiada reprezentację w Parlamencie Europejskim. Ugrupowanie tworzą w większości byli politycy Prawa i Sprawiedliwości, częściowo również Platformy Obywatelskiej. Przy partii działa także Stowarzyszenie Obywatelskie Polska Jest Najważniejsza, zarejestrowane w kwietniu 2011.')
        LPR=Party("Liga polskich rodzin",'',['nationalism','conservatism'],'','right','Liga Polskich Rodzin (LPR) – polska prawicowa partia polityczna, powstała 21 kwietnia 2001 (zarejestrowana sądownie 30 maja 2001) z połączenia Stronnictwa Narodowo-Demokratycznego i Stronnictwa Narodowego, których wspólne władze wybrano na I Kongresie LPR 5 maja 2001. W skład Komitetu Wyborczego Ligi Polskich Rodzin weszły także inne ugrupowania prawicy, m.in. Ruch Odbudowy Polski, Ruch Katolicko-Narodowy, Porozumienie Polskie i Przymierze dla Polski.')
        SP=Party("solidarna polska",'',['conservatism','christian_democrats'],'','right','Solidarna Polska Zbigniewa Ziobro (Solidarna Polska, SP, SPZZ) – polska prawicowa partia polityczna założona 24 marca 2012, zarejestrowana 1 czerwca 2012. Została utworzona przez działaczy opuszczających Prawo i Sprawiedliwość. Posiada klub parlamentarny w Sejmie VII kadencji i w Senacie VIII kadencji, założony przez grupę parlamentarzystów wybranych w wyborach parlamentarnych w 2011.')

        self.partylist=[SLD,PIS,PO,PRM,KPP,PSL,PJN,LPR,SP]
        self.down_screen.addstr(3,1,"Partie wygenerowane")
        self.refresh()
        lista_politykow = open("politycy.txt")
        imionameskie = open("imionameskie_UTF-8.txt").read().splitlines()
        imionadamskie = open("imionadamskie_UTF-8.txt").read().splitlines()
        nazwiska = open("nazwiska_UTF-8.txt").read().splitlines()
        self.clear()
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
            self.refresh()
            self.politycianslist.append(Politycian(imie,nazwisko,sex,random.randint(20,70),random.randint(0,100),random.randint(0,100),'',random.choice(self.ideologieslist),random.randint(0,100),random.randint(0,100),random.choice(['wysokie','niskie','srednie']),'',random.choice(self.partylist)))
        #zapisywanie polityków
        with open ('politycy.pickle', 'wb') as fp:
            pickle.dump(self.politycianslist, fp)
        
        self.down_screen.clear()
        #wczytywanie polityków
        with open ('politycy.pickle', 'rb') as fp:
            self.politycianslist = pickle.load(fp)
        self.partyChoosing()
    def politycianToParty(self):
        for i in range(len(self.partylist)):
            for x in range(len(self.politycianslist)):
                if (self.politycianslist[x].party.name==self.partylist[i].name): #&for t in range(len(self.partylist[i].members)):self.partylist[i].members[t]!=self.politycianslist[x]
                    self.partylist[i].members.append(self.politycianslist[x])

    def partyChoosing(self):
        self.clear()
        self.politycianToParty()
        self.up_screen.addstr(1,1,'Wybieranie Partii')
        position=0
        self.down_screen.addstr(11,1,"Wybieraj klawiszami ↑'o' i ↓'l' zatwierdzaj 'p'")
        while True:
            if (position<=0):position=0
            elif (position>=8):position=8
            for i in range(len(self.partylist)):
                if (i!=position):
                    self.down_screen.addstr(i+1,1,self.partylist[i].name)
                    self.refresh()
                elif (i==position):
                    self.down_screen.addstr(i+1,1,self.partylist[i].name,curses.color_pair(3))
                    self.refresh()
            

            key=self.ms.getch()
            if (key==ord('o')):
                position=position-1
            elif (key==ord('l')):
                position=position+1
            elif (key==ord('p')):
                self.partyInfo(position,True)
                break
    def partyInfo(self,ide,new_game):
        self.clear()
        self.up_screen.addstr(1,1,str(self.partylist[ide].name))
        self.down_screen.addstr(1,1,'Przewodniczący:'+str(self.partylist[ide].chairman))
        self.down_screen.addstr(2,1,'Podlądy:'+str(self.partylist[ide].views))
        self.down_screen.addstr(3,1,'Liczba czlonków:'+str(len(self.partylist[ide].members)))
        self.down_screen.addstr(4,1,'Doktryna:'+str(self.partylist[ide].doctrine))
        self.down_screen.addstr(5,0,'Opis:'+str(self.partylist[ide].description))
        self.refresh()
        if (new_game):
            self.up_screen.addstr(1, 1, 'aby wrócić, nacisnij "i", aby potwierzić wybór nacisnij "p"')
            self.refresh()
            while True:
                key=self.ms.getch()
                if (key==ord('i')):
                    self.partyChoosing()
                    break
                elif (key==ord('p')):
                    self.player.party=self.partylist[ide]
                    self.showPlayer(0)
                    break
        self.refresh()
    def showPlayer(self, mode):
        self.clear()
        self.up_screen.addstr(1,1,'Twoja postać:')
        self.down_screen.addstr(1, 1, 'Imię: '+self.player.name)
        self.down_screen.addstr(2, 1, 'Nazwisko: '+self.player.surname)
        self.down_screen.addstr(3, 1, 'Płeć: '+str(self.player.sex))
        self.down_screen.addstr(4, 1, 'Wiek: '+str(self.player.age))
        self.down_screen.addstr(5, 1, 'Partia: '+str(self.player.party.name))
        if (mode==0):
            self.down_screen.addstr(6, 1, 'Aby przejść do gry, naciśnij "p"\n Fabuła: Po udanym zamachu Brunona na sejm, ci którzy nie zginęli postanowili dać spokój polityce. To szansa dla nowego pokolenia polityków, takich jak ty!')
            while True:
                key=self.ms.getch()
                if (key==ord('p')):
                    self.mainGameMenu()
        self.refresh()
    def clear(self):
        self.up_screen.clear()
        self.down_screen.clear()
        self.up_screen.border(0)
        self.up_screen.refresh()
        self.down_screen.refresh()
        self.ms.refresh()
    def refresh(self):
        self.up_screen.refresh()
        self.down_screen.refresh()
        self.ms.refresh()
        
class Player():
    def __init__(self,name,surname,sex,age, party, popularity):
        self.age=age
        self.sex=sex
        self.name = name
        self.surname=surname
class Politycian():
    def __init__(self, name, surname, sex, age, popularity, truthfulness, eloquence, views, corruptibility, knowledgeofthelaw, education, profession, party):
        self.age=age
        self.sex=sex
        self.name = name
        self.surname=surname
        self.truthfulness=truthfulness
        self.eloquence=eloquence
        self.views=views
        self.corruptibility=corruptibility
        self.knowledgeofthelaw=knowledgeofthelaw
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
        
game= Game()
game.drawMainMenu()
