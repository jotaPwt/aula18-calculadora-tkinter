import tkinter as tk

def somar():
    n1 = float(input1.get())
    n2 = float(input2.get())
    soma = n1 + n2
    result.config(text= f'{soma}')

def subtracao():
    n1 = float(input1.get())
    n2 = float(input2.get())
    sub = n1 - n2
    result.config(text=f'({sub})')

def multiplicacao():
    n1 = float(input1.get())
    n2 = float(input2.get())
    mult = n1 * n2
    result.config(text= f'{mult}')

def divisao():
    n1 = float(input1.get())
    n2 = float(input2.get())
    div = n1 / n2
    result.config(text= f'{div}')
root = tk.Tk()


root.title('Calculadora')
root.geometry('300x500')

# label

texto = tk.Label(root, text= 'CALCULADORA')
texto.grid(row=1, column=3, pady=20)

# # input soma


input1 = tk.Entry(root)
input1.grid(row=3, column=7)

input2 = tk.Entry(root)
input2.grid(row=4, column=7)


# botao


botao = tk.Button(root, text='Soma', command = somar)
botao.grid(row=6, column=7, pady=2)


botao_sub = tk.Button(root, text='Subtração', command= subtracao)
botao_sub.grid(row=7, column=7, pady= 2)

botao_mult = tk.Button(root, text='Multiplicação', command= multiplicacao)
botao_mult.grid(row=8, column=7, pady=2)

botao_div = tk.Button(root, text='Divisão', command= divisao)
botao_div.grid(row=9, column= 7, pady=2)


# label

result = tk.Label(root, text='Resultado = ')
result.grid(row=10, column=7, pady=10)



root.mainloop()

