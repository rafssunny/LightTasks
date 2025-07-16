from customtkinter import *
from PIL import Image
from CTkMessagebox import CTkMessagebox
import webbrowser

janela = CTk()
janela.geometry('400x500')
janela.resizable(width=False, height=False)
janela.title('Light Tasks')
janela.iconbitmap('iconapp.ico')

#Variáveis
tasks_dict = {}
tasks_list = []
tasks_frame = []
#Funções)
def createtask():
    """
    Função para criar uma task no programa.
    :return: Task no menu principal com o nome inserido pelo usuário, juntamente com uma checkbox.
    """
    global nome_task, areatasks
    nome_da_task = nome_task.get()
    if not nome_da_task:
        CTkMessagebox(janela, message='Input a name on task.', icon='cancel', option_1='Ok', title='ERROR', fg_color='black', border_color='white', border_width=2, bg_color='black', button_color='white', button_text_color='black', button_hover_color='#b5b5b5', corner_radius=30, cancel_button='white', button_width=50)
    else:
        texto_centro.destroy()
        #frame principal
        areatasks = CTkFrame(scroll, width=400, height=50, border_width=2, border_color='white', fg_color='transparent')
        areatasks.pack(pady=5)
        areatasks.pack_propagate(False)
        tasks_frame.append(areatasks)

        #nome da task
        texto_nome = tasks_dict['Nome'] = nome_da_task
        if len(texto_nome) > 25:
            texto_nome = texto_nome[:25]+'...'
            texto_nome = texto_nome.capitalize()
        nome_icon = CTkImage(dark_image=Image.open('imgs/icontask.png'), size=(20, 20))
        nome_label = CTkLabel(areatasks, text=texto_nome, font=('comic sans ms', 20), image=nome_icon, compound='left')
        nome_label.place(relx=0.02, rely=0.18)

        #checkbox da task
        check_box = CTkCheckBox(areatasks, text='', onvalue='on', offvalue='off', width=30, height=30, fg_color='green', hover_color='#789D73', border_color='white')
        check_box.place(relx=0.90, rely=0.20)

        #Porcesso de lista e limpar entry
        tasks_list.append(tasks_dict.copy())
        tasks_dict.clear()
        nome_task.delete(0, END)
def deletetasks():
    """
    Função que deleta todas as tasks do usuário.
    :return: Todas as tasks até então feitas serão deletadas, desde que o usuário tenha criado ao menos uma task.
    """
    global areatasks
    if len(tasks_frame) == 0:
        CTkMessagebox(janela, message='You have not created any tasks.', icon='cancel', option_1='Ok',
                      title='ERROR', button_width=100, fg_color='black', bg_color='black',
                      button_color='white', button_text_color='black', button_hover_color='#b5b5b5', corner_radius=30,
                      cancel_button='white')
    else:
        check = CTkMessagebox(janela, message='Do you really want to delete all your tasks?', icon='warning', option_1='Yes', option_2='Cancel', title='WARNING', button_width=100, fg_color='black', bg_color='black', button_color='white', button_text_color='black', button_hover_color='#b5b5b5', corner_radius=30, cancel_button='white')
        if check.get() == 'Cancel':
            pass
            print(tasks_list)
        elif check.get() == 'Yes':
            tasks_list.clear()
            for frame in tasks_frame:
                frame.destroy()
        centro_img = CTkImage(dark_image=Image.open('imgs/pastaicon.png'), size=(60, 60))
        texto_centro = CTkLabel(scroll, text='All your created tasks appeared here', font=('comic sans ms', 20),
                                image=centro_img, compound='bottom')
        texto_centro.pack(pady=150)
        tasks_frame.clear()
def menuconfig():
    """
    Função que cria o menu de configurações.
    :return: Uma CTKtoplevel é criada com com informações sobre o programa.
    """
    global logo_image
    janela.withdraw()
    janela_config = CTkToplevel(janela, fg_color='black')
    janela_config.geometry('400x500')
    janela_config.title('LightTasks - Settings')
    janela_config.resizable(False, False)
    janela_config.iconbitmap('iconapp.ico')
    #Configs
    def exit():
        """
        Destrói a CtkToplevel e retorna a janela principal que havia sumido.
        :return: A Janela principal retorna.
        """
        janela_config.destroy()
        janela.deiconify()
    def entrartwitter():
        """
        Abrir a página do meu twitter e pegar o navegador padrão do computador do usuário
        :return: Abre a página do meu twitter.
        """
        navegador = webbrowser.get()
        navegador.open('https://x.com/rafssunny')
    #Designer
    #Frame principal
    main_frame = CTkFrame(janela_config, border_color='white', border_width=2, width=400, height=500, fg_color='black')
    main_frame.pack()
    main_frame.pack_propagate(False)
    #Logo programa
    imagem_app = CTkImage(dark_image=Image.open('./iconapp.ico'), size=(100,100))
    texto_topo = CTkLabel(main_frame, text='LightTasks 1.1', image=imagem_app, compound='bottom', font=('comic sans ms', 40), fg_color='black')
    texto_topo.pack(pady=5)
    texto_leave = CTkLabel(main_frame, text='You can exit settings pressing ESC or just closing the window', font=('comic sans ms', 12))
    texto_leave.pack(side='top')
    #Informações
    frame_um = CTkFrame(main_frame, width=350, height=270, fg_color='black', border_width=2, border_color='white')
    frame_um.pack(side='top')
    frame_um.pack_propagate(False)
    texto_save = CTkLabel(frame_um, text='All your files are saved automatically', font=('comic sans ms', 12))
    texto_save.pack(side='top', pady=10)
    texto_program = CTkLabel(frame_um, text='The program is under development and may\n present bugs, any problems contact me through my X\n\nClick on the cat', font=('comic sans ms', 12))
    texto_program.pack(side='top')
    gato_image = CTkImage(dark_image=Image.open('imgs/gatofundo.jpg'), size=(150,150))
    botao_gato = CTkButton(frame_um, text='', image=gato_image, fg_color='black', command=entrartwitter, hover_color='black')
    botao_gato.pack(side='top', pady=30)
    #Textocopyright
    texto_copyright = CTkLabel(main_frame, text='© 2025 rafssunny', font=('arial bold', 15))
    texto_copyright.pack()

    janela_config.protocol('WM_DELETE_WINDOW', exit)
    janela_config.bind("<Escape>", lambda event : exit())

def aumentoprogressbar():
    """
    Aumento da barra de progresso a medida que as tasks forem sendo feitas.
    :return: Sempre que uma task for feita um valor vai ser adicionado na barra de progresso, quando todas estiverem feitas ela ficará completa.
    """
    progresso = 1/len(tasks_list)

#Menu Principal
#Menu de Configurações de baixo
config_menu = CTkFrame(janela, width=400, height=50, fg_color='black', border_width=2, border_color='white')
config_menu.pack_propagate(False)
config_menu.pack(side='bottom')

#Botão configuração e Delete
config_image = CTkImage(dark_image=Image.open('imgs/configicon.png'), size=(20, 20))
config_button = CTkButton(config_menu, width=40, height=40, fg_color='white', text='', hover_color='#b5b5b5', image=config_image, command=menuconfig)
config_button.pack(side='right',padx=5)
delete_image = CTkImage(dark_image=Image.open('imgs/lixeiraicon.png'), size=(20, 20))
delete_button = CTkButton(config_menu, width=40, height=40, text='', image=delete_image, fg_color='#990000', hover_color='#3D0000', command=deletetasks)
delete_button.pack(side='right')

#Probressbar para as tasks
progress_bar = CTkProgressBar(config_menu, width=250, height=10, border_color='white', border_width=2, progress_color='#37FD12')
progress_bar.pack(side='left', padx=10)
progress_bar.set(0)

#Scroll Frame
scroll = CTkScrollableFrame(janela, width=400, height=390, fg_color='black', border_width=2, border_color='white', scrollbar_fg_color='black', scrollbar_button_color='white')
scroll.pack(side='bottom')

#Texto No Centro
centro_img = CTkImage(dark_image=Image.open('imgs/pastaicon.png'), size=(60, 60))
texto_centro = CTkLabel(scroll, text='All your created tasks appeared here', font=('comic sans ms', 20), image=centro_img, compound='bottom')
texto_centro.pack(pady=150)

#Menu de Criação no topo
opcoes = CTkFrame(janela, width=400, height=50, border_width=2, border_color='white', fg_color='black')
opcoes.place(relx=0,rely=0)
opcoes.pack_propagate(False)

#Entry com nome da Task
nome_task = CTkEntry(opcoes, width=150, placeholder_text='Task name...', fg_color='black', bg_color='black', border_color='white', corner_radius=25, border_width=2, placeholder_text_color='white')
nome_task.place(relx=0.50, rely=0.20)
nome_task.bind("<Return>", lambda event: createtask())

#Título
logo_image = CTkImage(dark_image=Image.open('./iconapp.ico'), size=(30,30))
mytasks_name = CTkLabel(opcoes, text='LightTasks', font=('comic sans ms', 20), fg_color='transparent', image=logo_image, compound='left')
mytasks_name.place(relx=0.03, rely=0.15)


#Botão Criar task
criartasks = CTkButton(opcoes, text='+', width=30, height=30, fg_color='white', corner_radius=10, hover_color='#b5b5b5', text_color='black',
                       command=createtask)
criartasks.place(relx=0.9, rely=0.19)

janela.mainloop()