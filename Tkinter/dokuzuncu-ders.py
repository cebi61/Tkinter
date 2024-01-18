import tkinter as tk 

form = tk.Tk()
form.title("Place")
form.geometry("500x450+250+250")
buton = tk.Button(text="Deneme",fg="red",bg="green",font="Times 17 bold")
# buton.place(relx=0.5,rely=0.5) #relx,rely= butonu forma göre hareket ettirir
buton.place(width=50,height=60) #butonun boyutlarını belirler


form.mainloop()