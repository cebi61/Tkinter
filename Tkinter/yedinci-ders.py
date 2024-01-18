import tkinter as tk 

form = tk.Tk()

form.title("Entry dersi")
form.geometry("500x450+250+250")

giris = tk.Entry(fg="red",bg="yellow") #kullanıcının giriş yapmasını sağlar
giris.pack()

giris2 = tk.Entry(form,fg="black",bg="blue") 
giris2.pack(side=tk.LEFT)


form.mainloop()