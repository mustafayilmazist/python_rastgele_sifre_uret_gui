# -*- conding: utf-8 -*-
'''
bu dosya python2.7 de yazılmıştır
mustafa yılmaz
'''
from tkinter import *
import random
import string
myPencere = Tk()
myPencere.geometry("400x300+100+200")
L1 = Label(myPencere, text="Sifre burada gozukecek")
L1.pack( side = LEFT)
E1 = Entry(myPencere, bd =1)
E1.pack(side = RIGHT)
def uret():
    basamak = E1.get()
    basamak = int(basamak)
    myMetin = ""
    for x in range(0,basamak):
        myMetin += random.choice(string.ascii_letters+string.digits)
    print("uretilen sifre:::", myMetin)
    L1.config(text=myMetin)
def kaydet():
    E1.config(text="abah")
myLable = Label(myPencere)
myLable.pack()
btnEkle = Button(text="Uret", command=uret)
btnEkle.pack()
mainloop()
