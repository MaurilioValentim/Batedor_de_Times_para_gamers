import customtkinter
from customtkinter import *
from PIL import Image, ImageTk


app = CTk()
app.title("Sorteador de Equipes")
app.geometry("1360x768")
set_appearance_mode("dark")

def exibir_mensagem():
    frame1 = CTkFrame(app, width=900, height=1300, corner_radius=0, fg_color="gray")
    frame1.place(relx=0.165, rely=0, relwidth=1, relheight=1)

btn = CTkButton(app, command=exibir_mensagem, text="Painel", corner_radius= 60)
btn.place(x=10, y=110)

#label_resultado = CTkLabel(app, text="")
#label_resultado.pack(pady=20)

#Carregar imagem
imagem = Image.open("trofeu.png")
imagem = imagem.resize((150, 150))
img_tk = ImageTk.PhotoImage(imagem)

#Adiciona a imagem em uma Label
label_imagem = CTkLabel(app, image=img_tk, text="")
label_imagem.place(relx=0.5, rely=0.5, anchor="center")


label_perfil = CTkLabel(app, text="Perfil", corner_radius= 80, fg_color="blue")
label_perfil.place(x=10, y=20)

app.mainloop()



