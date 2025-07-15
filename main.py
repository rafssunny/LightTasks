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
tasks_frame = []
#Funções)
def createtask():
    global nome_task, areatasks
    nome_da_task = nome_task.get()
    if not nome_da_task:
        CTkMessagebox(janela, message='Input a name on task.', icon='cancel', option_1='Ok', title='ERROR', fg_color='black', border_color='white', border_width=2, bg_color='black', button_color='white', button_text_color='black', button_hover_color='#b5b5b5', corner_radius=30, cancel_button='white', button_width=50)
    else:
        #frame principal
        areatasks = CTkFrame(scroll, width=400, height=50, border_width=2, border_color='white', fg_color='transparent')
        areatasks.pack(pady=5)
        areatasks.pack_propagate(False)
        tasks_frame.append(areatasks)

        #nome da task
        texto_nome = tasks_dict['Nome'] = nome_da_task
        if len(texto_nome) > 25:
            texto_nome = texto_nome[:25]+'...'
        nome_icon = CTkImage(dark_image=Image.open('./icontask.png'), size=(20,20))
        nome_label = CTkLabel(areatasks, text=texto_nome, font=('comic sans ms', 20), image=nome_icon, compound='left')
        nome_label.place(relx=0.02, rely=0.18)

        #checkbox da task
        check_box = CTkCheckBox(areatasks, text='', onvalue='on', offvalue='off', width=30, height=30, fg_color='green')
        check_box.place(relx=0.90, rely=0.20)

        tasks_list.append(tasks_dict.copy())
        tasks_dict.clear()
        nome_task.delete(0, END)
def deletetasks():
    global areatasks
    check = CTkMessagebox(janela, message='Você quer realmente deletar todas as suas tasks?', icon='warning', option_1='Yes', option_2='Cancel', title='WARNING', button_width=100, fg_color='black', bg_color='black', button_color='white', button_text_color='black', button_hover_color='#b5b5b5', corner_radius=30, cancel_button='white')
    if check.get() == 'Cancel':
        pass
        print(tasks_list)
    elif check.get() == 'Yes':
        tasks_list.clear()
        for frame in tasks_frame:
            frame.destroy()

#Menu Principal
#Menu de Configurações de baixo
config_menu = CTkFrame(janela, width=400, height=50, fg_color='black', border_width=2, border_color='white')
config_menu.pack_propagate(False)
config_menu.pack(side='bottom')

#Botão configuração e Delete
config_image = CTkImage(dark_image=Image.open('./configicon.png'), size=(20,20))
config_button = CTkButton(config_menu, width=40, height=40, fg_color='white', text='', hover_color='#b5b5b5', image=config_image)
config_button.pack(side='right',padx=5)
delete_image = CTkImage(dark_image=Image.open('./lixeiraicon.png'), size=(20,20))
delete_button = CTkButton(config_menu, width=40, height=40, text='', image=delete_image, fg_color='#990000', hover_color='#3D0000', command=deletetasks)
delete_button.pack(side='right')
#Probressbar para as tasks
progress_bar = CTkProgressBar(config_menu, width=250, height=10, border_color='white', border_width=2, progress_color='#37FD12')
progress_bar.pack(side='left', padx=10)
progress_bar.set(0)
#Scroll Frame
scroll = CTkScrollableFrame(janela, width=400, height=390, fg_color='black', border_width=2, border_color='white', scrollbar_fg_color='black', scrollbar_button_color='white')
scroll.pack(side='bottom')

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


#Botões
criartasks = CTkButton(opcoes, text='+', width=30, height=30, fg_color='white', corner_radius=10, hover_color='#b5b5b5', text_color='black',
                       command=createtask)
criartasks.place(relx=0.9, rely=0.19)
janela.mainloop()