import customtkinter
from customtkinter import *
from PIL import Image, ImageTk


app = CTk()
app.title("Sorteador de Equipes")
app.geometry("1360x768")
set_appearance_mode("dark-blue")

def exibir_mensagem():
    frame1 = CTkFrame(app, width=900, height=1300, corner_radius=0, fg_color="#EBEBEB")
    frame1.place(relx=0.165, rely=0, relwidth=1, relheight=1)


def listagem_jogadores():
    frame_lista = CTkFrame(app, width=900, height=1300, corner_radius=0, fg_color="#EBEBEB")
    frame_lista.place(relx=0.165, rely=0, relwidth=1, relheight=1)

    label_titulo = CTkTextbox(frame_lista, width=300, height=200)
    label_titulo.place(relx=0.15, rely=0.15)

#label_resultado = CTkLabel(app, text="")
#label_resultado.pack(pady=20)

frame_principal = CTkFrame(app, width=221, height=900, fg_color="#2a8c56")
frame_principal.place(x=0, y=0)

btn_painel = CTkButton(app, width=221, height=150, command=exibir_mensagem, text="Painel", corner_radius= 0, hover_color="white")
btn_painel.place(x=0, y=0)

btn_perfil = CTkButton(app, width=221, height=50, command=listagem_jogadores, text="Lista de Jogadores", corner_radius= 0, hover_color="white")
btn_perfil.place(x=0, y=150)




#Carregar imagem
#imagem = Image.open("trofeu.png")
#imagem = imagem.resize((150, 150))
#img_tk = ImageTk.PhotoImage(imagem)

#Adiciona a imagem em uma Label
#label_imagem = CTkLabel(app, image=img_tk, text="")
#label_imagem.place(relx=0.5, rely=0.5, anchor="center")



app.mainloop()



