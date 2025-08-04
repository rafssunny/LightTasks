from customtkinter import *
from PIL import Image
from CTkMessagebox import CTkMessagebox
def centralizar(janela, largura, altura):
    """
    Centraliza a Janela criada no monitor do usuário.
    :param janela: Nome da janela CTk que vai ser centralizada
    :param largura: largura da janela
    :param altura: altura da janela
    :return: A tela centralizada de acordo com o tamanho do monitor do usuário
    """
    largura_janela = largura
    altura_janela = altura
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = int((largura_tela/2) - int(largura_janela/2))
    pox_y = int((altura_tela/2) - int(altura_janela/2))
    janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pox_y}')
def menupersonagem():
    menu = CTk()
    menu.title('Character Customization')
    menu.iconbitmap('iconapp.ico')
    menu.resizable(False, False)
    centralizar(menu, 500, 500)
    #  Area personagem
    area_personagem = CTkFrame(menu, width=250, height=400, border_width=2, border_color='white')
    area_personagem.place(relx=0,rely=0)
    area_personagem.pack_propagate(False)
    nome_personagem = CTkEntry(area_personagem, width=200, height=50, border_width=2, border_color='white', placeholder_text='Name...')
    nome_personagem.pack(side='bottom', pady=10)
    #  Area status
    area_status = CTkFrame(menu, width=250, height=100, border_width=2, border_color='white')
    area_status.place(relx=0,rely=0.8)
    area_status.pack_propagate(False)
    vida = CTkLabel(area_status, text='Hearts', text_color='#D0312D', font=('comic sans ms', 20))
    vida.place(relx=0.1,rely=0.1)
    mana = CTkLabel(area_status, text='Mana', text_color='#3944BC', font=('comic sans ms', 20))
    mana.place(relx=0.6, rely=0.1)
    atk = CTkLabel(area_status, text='Atk', text_color='#FCA510', font=('comic sans ms', 20))
    atk.place(relx=0.1,rely=0.6)
    defesa = CTkLabel(area_status, text='Def', text_color='#7DC069', font=('comic sans ms', 20))
    defesa.place(rely=0.6, relx=0.6)
    #  Area visuais
    area_visuais = CTkScrollableFrame(menu, width=230, height=500, border_width=2, border_color='white')
    area_visuais.pack(side='right')
    menu.mainloop()
menupersonagem()