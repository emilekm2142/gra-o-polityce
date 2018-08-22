# -*- coding: utf-8 -*-
import codecs
 
try:
    # Python 2.x. Jesieli używamy Pythona > 2.x, bedzie exception.
    from tkFileDialog import askopenfilename
    from Tkinter import Tk, LabelFrame, Button, OptionMenu, StringVar
except ImportError:
    # Python 3.x
    from tkinter.filedialog import askopenfilename
    from tkinter import Tk, LabelFrame, Button, OptionMenu, StringVar
 
### Funkcja, która otwiera okienko po wybrania zestaw znaków
### Tylko w Python 3.x można ją naziwać wybierajZestawZnaków, więc zostawiamy wybierajZestawZnakow
def wybierajZestawZnakow(zestawieZnakow):
    gui = Tk()
    gui.resizable(0, 0)
    gui.title("")
    fra1 = LabelFrame(gui, text="Stary zestaw znaków")
    fra1.pack(padx=2, pady=2)
    var1 = StringVar()
    var1.set(zestawieZnakow[0])
    opt1 = OptionMenu(fra1, var1, *zestawieZnakow)
    opt1.pack(fill="x")
    but1 = Button(fra1, text="Otwieraj plik", command=lambda:gui.destroy())
    but1.pack(fill="x", padx=2, pady=2)
    gui.mainloop()
    return var1.get()
 
##Zaczyna się program
 
zestawieZnakow = ("windows-1250", "iso-8859-2", "windows-1252") # są inne kodowanie ...
stareKodowaniePliku = wybierajZestawZnakow(zestawieZnakow) #użytkownik wybiera kodowanie...
 
imiePlikuOrigynalnego = askopenfilename() # użytkownik wybiera plik
plikOrigynalny = codecs.open(imiePlikuOrigynalnego, 'r', stareKodowaniePliku)
 
ostatkniaKropka = imiePlikuOrigynalnego.rfind(".") #po ostatniej kropki zaczyna się rozszerzenie
imieNowegoPliku = imiePlikuOrigynalnego[:ostatkniaKropka] + "_UTF-8"+imiePlikuOrigynalnego[ostatkniaKropka:]
 
nowyPlik = codecs.open(imieNowegoPliku, 'w', 'utf-8')
 
for kreska in plikOrigynalny.readlines():
    nowyPlik.write(kreska) # kreska "windows-1250 (albo inna)" --> do pliku UTF-8  => ąćęńłośżźĄĆĘŃŁÓŚŻŹ
 
plikOrigynalny.close()
nowyPlik.close()
