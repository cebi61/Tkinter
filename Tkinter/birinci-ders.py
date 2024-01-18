import tkinter as tk    #tkinter kütüphanesini çağırır
form = tk.Tk()      #form oluşturur
form.title("Tkinter Dersleri-1")    #başlığı değiştirir
etiket=tk.Label(text="Tkinter Python")  #label oluşturur
etiket.pack()   #label ı sabitler
etiket2 = tk.Label(form,text="Python Tkinter Dersleri") #Label oluşturur. parentez içindeki form labe ın konumunu gösterir
etiket2.pack()

form.mainloop()

