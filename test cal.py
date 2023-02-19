from tkinter import *
from tkinter import ttk


# cores 
cor1 = "#21130d"  # preto
cor2 = "#1d0d21"  # roxo escuro
cor3 = "#e9e7e7"  # branco cinza
cor4 = "#4d423d"  # marrom bem clarinho 
cor5 = "#044836"  # verde musgo


# Criando a janela
Janela =Tk()
Janela.title("Calculadora")
Janela.geometry("235x310")
Janela.config(bg=cor2)


# Criando Frames 
Frame_tela = Frame(Janela, width=235, height=50, bg=cor4)
Frame_tela.grid(row=0, column=0)

Frame_corpo = Frame(Janela, width=235, height=268, bg=cor2)
Frame_corpo.grid(row=1, column=0)


# Variavel Todos Valores 

todos_valores = ''


valor_texto = StringVar()


# Criando Função

def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)


    #passando valor para tela
    valor_texto.set(todos_valores)

    # Função Limpa Tela

def limpa_tela():
    global todos_valores 
    todos_valores=""
    valor_texto.set("")

# Função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))











# Criando painel de resultados



app_label = Label(Frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('ivy 17 bold'), bg=cor2, fg=cor3)
app_label.place(x=0, y=0)



# Criando botoes
b_1 = Button(Frame_corpo,command = limpa_tela, text="C", width=11, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(Frame_corpo, command = lambda: entrar_valores('%'),text="%", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(Frame_corpo, command = lambda: entrar_valores('/'),text="/", width=5, height=2, bg=cor5,fg=cor3, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(Frame_corpo, command = lambda: entrar_valores('7'),text="7", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(Frame_corpo, command = lambda: entrar_valores('8'),text="8", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52)

b_6 = Button(Frame_corpo, command = lambda: entrar_valores('9'),text="9", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=52)

b_7 = Button(Frame_corpo, command = lambda: entrar_valores('4'),text="4", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=104)

b_8 = Button(Frame_corpo, command = lambda: entrar_valores('5'),text="5", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=60, y=104)

b_9 = Button(Frame_corpo, command = lambda: entrar_valores('6'),text="6", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=120, y=104)

b_10 = Button(Frame_corpo, command = lambda: entrar_valores('1'),text="1", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=0, y=156)

b_11 = Button(Frame_corpo, command = lambda: entrar_valores('2'),text="2", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=60, y=156)

b_12 = Button(Frame_corpo, command = lambda: entrar_valores('3'),text="3", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=120, y=156)

b_13 = Button(Frame_corpo, command = lambda: entrar_valores('0'),text="0", width=11, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=208)

b_14 = Button(Frame_corpo, command = lambda: entrar_valores('%'),text=".", width=5, height=2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=208)


# Teclas de função

b_15 = Button(Frame_corpo, command = lambda: entrar_valores('*'),text="*", width=5, height=2, bg=cor5,fg=cor3, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=52)

b_15 = Button(Frame_corpo, command = lambda: entrar_valores('-'),text="-", width=5, height=2, bg=cor5,fg=cor3, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=104)

b_15 = Button(Frame_corpo, command = lambda: entrar_valores('+'),text="+", width=5, height=2, bg=cor5,fg=cor3, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_15 = Button(Frame_corpo, command =calcular,text="=", width=5, height=2, bg=cor5,fg=cor3, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=208)















Janela.mainloop()