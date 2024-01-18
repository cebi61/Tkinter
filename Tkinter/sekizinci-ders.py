#side= left-right-top-bottom
#fill= x-y
#expand= 0-1, konumunu sabitler
#anchor= "n" yukarı, "s" aşağı, "e" sağ, "w" sol, "ne" yukarı sağ, "nw" yukarı sol, "se" asağı sağ, "sw" aşağı sol, "center" orta
#padx,pady = butonu konumunu yanına sayı yazarak belirler
#ipadx,ipady = butonun boyutunu yanına sayı yazarak belirler

import tkinter as tk 

form = tk.Tk()
form.geometry("500x500")
form.title("Sekizinci ders")

label = tk.Label(text="geometrik yöneticiler")
label.pack(side=tk.LEFT)

buton = tk.Button(text="pack()",bg="red")
# buton.pack(side=tk.BOTTOM, fill=tk.X,expand=tk.YES)
# buton.pack(expand=tk.YES,anchor="se")

# buton.pack(padx=20,pady=50) 
buton.pack(ipadx=20,ipady=50)


form.mainloop()