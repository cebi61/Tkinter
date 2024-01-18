import tkinter as tk

form=tk.Tk()
form.title("Tkinter Dersleri Formu")
label=tk.Label(form,text="Python Tkinter")
label.pack()
label2=tk.Label(form,text="Ders-2",fg="red") #fg renk belirmede kullanılır.
label2.pack()
label3=tk.Label(form,text="Ders-2 arka plan",fg="black",bg="green") #bg label ın arka planını renklerndirir
label3.pack()
label4=tk.Label(form,text="yeni label",fg="red",bg="blue",font="Times 15 italic") #'fonr' label ın yazı tipini boyutunu ve genel tipini belirleyebiliriz
label4.pack()
label5=tk.Label(form,text="En son Label",fg="green",bg="red",font="Times 17 bold")
label5.pack()
form.mainloop()