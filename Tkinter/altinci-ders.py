import tkinter as tk 
import random as rd 

form = tk.Tk()
form.title("Tekrar Uygulaması")
form.geometry("500x400+500+350")

liste = []
for i in range(5):
    while len(liste) !=6:
        a = rd.randint(1,50)
        if a not in liste:
            liste.append(a)

def göster():
    label.config(text=liste,bg="green")

def saydamlastir():
    form.wm_attributes("-alpha",0.3)
def dondur():
    form.wm_attributes("-alpha",0.9)
    
def maxyap():
    form.state("zoomed")
def minyap():
    form.state("iconic")

label = tk.Label(form,fg="red",bg="red",font="Times 20 bold")
label.pack()

göster = tk.Button(form,text="Göster",fg="black",bg="yellow",command=göster)
göster.pack(side=tk.LEFT)

saydamlastir_button = tk.Button(form, text="Saydamlaştır", fg="black", bg="yellow", command=saydamlastir)
saydamlastir_button.pack(side=tk.LEFT)



dondur_button = tk.Button(form, text="Döndür", fg="black", bg="yellow", command=dondur)
dondur_button.pack(side=tk.LEFT)


minyap = tk.Button(form,text="minyap",fg="black",bg="yellow",command=minyap)
minyap.pack(side=tk.LEFT)

maxyap = tk.Button(form,text="maxyap",fg="black",bg="yellow",command=maxyap)
maxyap.pack(side=tk.LEFT)

form.mainloop()