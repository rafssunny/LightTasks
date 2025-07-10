from customtkinter import *
from PIL import Image
from CTkMessagebox import CTkMessagebox

janela = CTk()
janela.geometry('400x500')
janela.resizable(width=False, height=False)
janela.title('Light Tasks')
janela.iconbitmap('iconapp.ico')

#Variáveis
tasks_dict = {}
tasks_list = []
check = 0
n1 = 0
n2 = 0.1
#Funções)
def janelacreatetask():
    def createtask():
        global check, n1, n2
        if n2 == 0.7:
            CTkMessagebox(title='ERRO', message='Limite de Tasks atingidas, limpe o cachê para continuar.', icon='cancel', option_1='Ok')
        else:
            if check != 0:
                n2+=0.1
            areatasks = CTkFrame(janela, width=400, height=50, border_width=2, border_color='white')
            areatasks.place(relx=n1, rely=n2)
            areatasks.pack_propagate(False)

            texto_nome = tasks_dict['Nome'] = nome.get()
            tasks_dict['Tempo'] = tempo.get()
            if len(texto_nome) > 20:
                texto_nome = texto_nome[:20]+'...'
            nome_icon = CTkImage(dark_image=Image.open('./icontask.png'), size=(20,20))
            nome_label = CTkLabel(areatasks, text=texto_nome, font=('comic sans ms', 20), image=nome_icon, compound='left')
            nome_label.place(relx=0.02, rely=0.18)

            tempo_icon = CTkImage(dark_image=Image.open('./icontime.png'), size=(25,25))
            tempo_label = CTkLabel(areatasks, text=tasks_dict['Tempo']+'H', font=('comic sans ms', 20), wraplength=300, image=tempo_icon,
                                   compound='left')
            tempo_label.place(relx=0.85,rely=0.18)

            tasks_list.append(tasks_dict.copy())
            tasks_dict.clear()
            check+=1
            print(n2)

    janela_task = CTkToplevel(janela, fg_color='black')
    janela_task.geometry('400x200')
    janela_task.title('Create Task')
    janela_task.resizable(width=False, height=False)
    janela_task.iconbitmap('iconapp.ico')

    ceu_imagem = CTkImage(dark_image=Image.open('./fundo.jpg'), size=(400, 500))
    ceu_imagemlabel = CTkLabel(janela_task, width=400, height=200, image=ceu_imagem, text='')
    ceu_imagemlabel.place(relx=0.0, rely=0.0)

    nome = CTkEntry(janela_task, width=200, placeholder_text='Nome da Task...', fg_color='black', bg_color='black', border_color='black')
    nome.pack(pady=20)

    tempo = CTkEntry(janela_task, width=200, placeholder_text='Tempo Total em Horas...', fg_color='black', bg_color='black', border_color='black')
    tempo.pack(pady=10)

    botao_ok = CTkButton(janela_task, width=50, height=20, text='Create', fg_color='#90ee90', font=('comic sans ms', 20),
                         hover_color='#006400', border_color='#90ee90', text_color='black', command=createtask, border_width=0,
                         corner_radius=0)
    botao_ok.pack(pady=20)


#Menu Principal
#Fundo
ceu_imagem = CTkImage(dark_image=Image.open('./fundo.jpg'), size=(400,500))
ceu_imagemlabel = CTkLabel(janela, width=200, height=200, image=ceu_imagem, text='')
ceu_imagemlabel.place(relx=0.0,rely=0.0)

#Textos
opcoes = CTkFrame(janela, width=400, height=50, border_width=2, border_color='white')
opcoes.place(relx=0,rely=0)
opcoes.pack_propagate(False)

mytasks_name = CTkLabel(opcoes, text='M y T  a  s  k  s', font=('comic sans ms', 20), fg_color='transparent')
mytasks_name.place(relx=0.04, rely=0.15)

#Botões
criartasks = CTkButton(opcoes, text='+', width=30, height=30, fg_color='#90ee90', corner_radius=10, hover_color='#006400', text_color='black',
                       command=janelacreatetask)
criartasks.place(relx=0.9, rely=0.15)
janela.mainloop()