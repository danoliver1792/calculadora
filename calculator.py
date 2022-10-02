from tkinter import *
from tkinter import ttk
import math

# Cores da calculadora
colorOne = '#3b3b3b'
colorTwo = '#feffff'
colorThree = '#37474F'
colorFour = '#252c36'
colorFive = '#FFAB40'
colorSix = '#098530'

# Janela principal:
windown = Tk()
windown.title('Calculadora')
windown.geometry('235x287')
windown.config(bg=colorOne)

# Criação dos frames (tela com resultado, teclas e corpo da calculadora)
frame_screen = Frame(windown, width=300, height=56, bg=colorThree)
frame_screen.grid(row=0, column=0)

frame_scientific = Frame(windown, width=300, height=86)
frame_scientific.grid(row=1, column=0)

frame_body = Frame(windown, width=300, height=340)
frame_body.grid(row=2, column=0)

# Funcionalidades
global allValues

allValues = ''
textView = StringVar()

# Entrar valores na tela
def enterValues(event):
    global allValues
    
    allValues = allValues + str(event)
    textView.set(allValues)
    

# Calculos
def calculate():
    global allValues
        
    modules = ['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log', 'math.factorial', 'math.e', 'math.pow', 'math.pi']

    for i in modules:
        if i == 'math.tan':
            allValues = allValues.replace('tan', i)
        elif i == 'math.sin':
            allValues = allValues.replace('sin', i)
        elif i == 'math.cos':
            allValues = allValues.replace('cos', i)
        elif i == 'math.sqrt':
            allValues = allValues.replace('sqrt', i)
        # -----------------------------------------
        elif i == 'math.log':
            allValues = allValues.replace('log', i)
        elif i == 'math.factorial':
            allValues = allValues.replace('factorial', i)
        elif i == 'math.e':
            allValues = allValues.replace('e', i)
        elif i == 'math.pow':
            allValues = allValues.replace('pow', i)
        # -----------------------------------------
        elif i == 'math.pi':
            allValues = allValues.replace('pi', i)
    
    result = str(eval(allValues))
    textView.set(result)
    
    allValues = ''


# Limpar tela
def delete():
    global allValues
    allValues = ''
    textView.set('')
    
    
# configuração do frame(screen) o que irá imprimir na tela
label_screen = Label(frame_screen, textvariable=textView, width=16, height=2, padx=7, anchor='e', bd=0, justify=RIGHT, bg=colorThree, font=('Ivy 18'), fg=colorTwo)
label_screen.place(x=0, y=0)

# configuração do frame(scientific). Daqui vão sair os botões
b_0 = Button(frame_scientific, command=lambda:enterValues('tan'), text='tan', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_0.place(x=0, y=0)

b_1 = Button(frame_scientific, command=lambda:enterValues('sin'), text='sin', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_1.place(x=59, y=0)

b_2 = Button(frame_scientific, command=lambda:enterValues('cos'), text='cos', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_2.place(x=118, y=0)

b_3 = Button(frame_scientific, command=lambda:enterValues('sqrt'), text='√', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_3.place(x=177, y=0)

# Segunda linha de botões
b_0 = Button(frame_scientific, command=lambda:enterValues('log'), text='log', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_0.place(x=0, y=29)

b_1 = Button(frame_scientific, command=lambda:enterValues('factorial'), text='!', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_1.place(x=59, y=29)

b_2 = Button(frame_scientific, command=lambda:enterValues('e'), text='e', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_2.place(x=118, y=29)

b_3 = Button(frame_scientific, command=lambda:enterValues('pow'), text='pow', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_3.place(x=177, y=29)

# Terceira linha de botões
b_0 = Button(frame_scientific, command=lambda:enterValues('pi'), text='π', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_0.place(x=0, y=58)

b_1 = Button(frame_scientific, command=lambda:enterValues(','), text=',', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_1.place(x=59, y=58)

b_2 = Button(frame_scientific, command=lambda:enterValues('('), text='(', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_2.place(x=118, y=58)

b_3 = Button(frame_scientific, command=lambda:enterValues(')'), text=')', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_3.place(x=177, y=58)


# Quarta linha de botões
b_0 = Button(frame_body, command=delete, text='C', width=14, height=1, relief=RAISED, overrelief=RIDGE, bg=colorSix, font=('Ivy 10 bold'), fg=colorTwo)
b_0.place(x=0, y=0)

b_1 = Button(frame_body, command=lambda:enterValues('//'), text=':', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_1.place(x=118, y=0)

b_2 = Button(frame_body, command=lambda:enterValues('/'), text='÷', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_2.place(x=177, y=0)

# Quinta linha de botões
b_0 = Button(frame_body, command=lambda:enterValues('7'), text='7', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_0.place(x=0, y=29)

b_1 = Button(frame_body, command=lambda:enterValues('8'), text='8', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_1.place(x=59, y=29)

b_2 = Button(frame_body, command=lambda:enterValues('9'), text='9', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_2.place(x=118, y=29)

b_3 = Button(frame_body, command=lambda:enterValues('*'), text='x', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_3.place(x=177, y=29)

# Sexta linha de botões
b_0 = Button(frame_body, command=lambda:enterValues('4'), text='4', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_0.place(x=0, y=58)

b_1 = Button(frame_body, command=lambda:enterValues('5'), text='5', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_1.place(x=59, y=58)

b_2 = Button(frame_body, command=lambda:enterValues('6'), text='6', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_2.place(x=118, y=58)

b_3 = Button(frame_body, command=lambda:enterValues('-'), text='-', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_3.place(x=177, y=58)

# Sétima linha de botões
b_0 = Button(frame_body, command=lambda:enterValues('1'), text='1', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_0.place(x=0, y=87)

b_1 = Button(frame_body, command=lambda:enterValues('2'), text='2', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_1.place(x=59, y=87)

b_2 = Button(frame_body, command=lambda:enterValues('3'), text='3', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_2.place(x=118, y=87)

b_3 = Button(frame_body, command=lambda:enterValues('+'), text='+', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_3.place(x=177, y=87)

# Oitava linha de botões
b_0 = Button(frame_body, command=lambda:enterValues('0'), text='0', width=14, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_0.place(x=0, y=116)

b_1 = Button(frame_body, command=lambda:enterValues('.'), text='.', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_1.place(x=118, y=116)

b_2 = Button(frame_body, command=calculate, text='=', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=colorFour, font=('Ivy 10 bold'), fg=colorTwo)
b_2.place(x=177, y=116)

# Chamando a calculadora
windown.mainloop()
