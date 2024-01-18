import tkinter as tk

form=tk.Tk()
form.title("Tkinter Dersleri Ders-3")
form.geometry("500x250+500+350") #formu boyutlandırmaya yarar(ilk ikisi), formun gelicek konumunu belirler(son ikisi)
form.resizable(False,True) #hem "x" hem de "y" ekseniyle oynanılmasına izin verip vermemeye yarıyor 

# form.minsize(450,400) #formun boyutunu minimilize eder
# form.maxsize(550,550) #formun boyutunu maximilize eder


label = tk.Label(form,text="Ders-3-")
label.pack()

form.mainloop()