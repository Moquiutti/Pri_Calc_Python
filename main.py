from tkinter import *

root = Tk()
root.title('Sua calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

numero1=''
divisao = FALSE

root.configure(background='#282828')

e = Entry(root,
          width=15,
          borderwidth=FLAT,
          fg='#FFFFFF',
          font=('futura', 25, 'bold'),
          justfy=CENTER)
e.grid(row=0, column=0, columnspan=4, pady=2)


  #funções operadores
  
def botao_divisao():
  global numero1
  global divisão
  divisao = True
  numero1 = e.get()
  e.delete(0,END)
  
def botao_multiplicacao():
  global numero1
  global multiplicacao
  multiplicacao = True
  numero1 = e.get()
  e.delete(0,END)
  
def botao_menos():
  global numero1
  global muenos
  menos = True
  numero1 = e.get()
  e.delete(0,END)
  
def botao_mais():
  global numero1
  global mais
  mais = True
  numero1 = e.get()
  e.delete(0,END)
  
def botao_limpa():
  e.delete(0, END)

def botao_igual():
  global adicao
  global subtracao
  global multiplicacao
  global divisao
  numero2 = e.get()
  e.delete(0, END)
  
if adicao == TRUE:
  e.insert(0, int(numero1) + int(numero2))
  adicao = FALSE
  
if menos == TRUE:
  e.insert(0, int(numero1) - int(numero2))
  menos = FALSE
  
if multiplicacao == TRUE:
  e.insert(0, int(numero1) * int(numero2))
  multiplicacao = FALSE

if divide == TRUE:
  e.insert(0, int(numero1) / int(numero2))
  divide = FALSE
  
def botao_click(num):
  e.insert(END, num)

divide = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao(),
                fg='#FFFFFFF',
                activebackground='#FFFFFFF',
                bg='#320064',
                activeforeground='#240046',
                reliefe=FLAT,
                font=('futura', 12, 'bold'))
divide.grid(row=0, column=4)

  #primeira fileira

um = Button(root,
            text='1',
            padx=40,
            pady=20,
            command=lambda: botao_click(1),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
um.grid(row=1, column=1)
dois = Button(root,
            text='2',
            padx=40,
            pady=20,
            command=lambda: botao_click(2),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
dois.grid(row=1, column=2)
tres = Button(root,
            text='3',
            padx=40,
            pady=20,
            command=lambda: botao_click(3),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
tres.grid(row=1, column=3)
multiplicacao = Button(root,
            text='*',
            padx=40,
            pady=20,
            command=botao_multiplicacao(),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
multiplicacao.grid(row=1, column=4)

  #segunda fileira

quatro = Button(root,
            text='4',
            padx=40,
            pady=20,
            command=lambda: botao_click(4),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
botao_click.grid(row=2, column=1)
cinco = Button(root,
            text='5',
            padx=40,
            pady=20,
            command=lambda: botao_click(5),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
botao_click.grid(row=2, column=2)
seis = Button(root,
            text='6',
            padx=40,
            pady=20,
            command=lambda: botao_click(6),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
botao_click.grid(row=2, column=3)
menos = Button(root,
            text='-',
            padx=40,
            pady=20,
            command=botao_menos(),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
menos.grid(row=2, column=4)

#terceira fileira 

sete = Button(root,
            text='7',
            padx=40,
            pady=20,
            command=lambda: botao_click(7),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
sete.grid(row=3, column=1)

oito = Button(root,
            text='8',
            padx=40,
            pady=20,
            command=lambda: botao_click(8),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
botao_click.grid(row=3, column=2)

nove = Button(root,
            text='9',
            padx=40,
            pady=20,
            command=lambda: botao_click(9),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
botao_click.grid(row=3, column=3)

mais = Button(root,
            text='+',
            padx=40,
            pady=20,
            command=botao_mais(),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
mais.grid(row=3, column=4)
#Quarta Fileira 
zero = Button(root,
            text='0',
            padx=40,
            pady=20,
            command=lambda: botao_click(0),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
zero.grid(row=3, column=3, columnspan=2)

limpa = Button(root,
            text='c',
            padx=40,
            pady=20,
            command=botao_limpa(),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
limpa.grid(row=4, column=3)

igual = Button(root,
            text='=',
            padx=40,
            pady=20,
            command=botao_igual(),
            fg='#FFFFFFF',
            activebackground='#FFFFFFF',
            bg='#320064',
            activeforeground='#240046',
            reliefe=FLAT,
            font=('futura', 12, 'bold'))
igual.grid(row=4, column=4)

root.mainloop()