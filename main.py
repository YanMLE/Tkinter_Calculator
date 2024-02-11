import tkinter as tk


def clique_butão(symbol):
    current = display.get()
    if current == "Error":
        display.set("")

    if current and current[-1].isdigit() and symbol == '(':
        display.set(current + '*' + symbol)
    elif current and current[-1] == ")" and symbol == '(':
        display.set(current + '*' + symbol)
    elif current and current[-1] == ")" and symbol.isdigit():
        display.set(current + '*' + symbol)
    elif current == "" and symbol in ['+', '', '/', '/100', '**2']:
        display.set("0" + symbol)
    else:
        display.set(current + symbol)


def calcular():
    try:
        result = eval(display.get())
        display.set(result)
    except Exception as e:
        display.set("Error")


def apagar():
    display.set("")


root = tk.Tk()
root.title("Calculadora")
root.configure(bg='black')

display = tk.StringVar()
display.set("")

entry = tk.Entry(root, textvariable=display, font=('Arial', 25), justify='right', bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=5, sticky='nsew')

butões = [

    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('+', 4, 3),
    ('(', 5, 0), ('0', 5, 1), (')', 5, 2),
]
for (text, row, col) in butões:
    btn = tk.Button(root, text=text, font=('Arial', 20), bg='black', fg='white', command=lambda t=text: clique_butão(t))
    btn.grid(row=row, column=col, sticky='nsew')

mais_btn = tk.Button(root, text='+', font=('Arial', 20), command=lambda: clique_butão("+"), bg='black', fg='#FF85FF')
mais_btn.grid(row=4, column=3, sticky='nsew')

menos_btn = tk.Button(root, text='-', font=('Arial', 20), command=lambda: clique_butão("-"), bg='black', fg='#FF85FF')
menos_btn.grid(row=3, column=3, sticky='nsew')

vezes_btn = tk.Button(root, text='×', font=('Arial', 20), command=lambda: clique_butão("*"), bg='black', fg='#FF85FF')
vezes_btn.grid(row=2, column=3, sticky='nsew')

dividir_btn = tk.Button(root, text='÷', font=('Arial', 20), command=lambda: clique_butão("/"), bg='black', fg='#FF85FF')
dividir_btn.grid(row=1, column=3, sticky='nsew')

quadrado_btn = tk.Button(root, text='X²', font=('Arial', 20), command=lambda: clique_butão("**2"), bg='black',
                         fg='#FF85FF')
quadrado_btn.grid(row=1, column=2, sticky='nsew')

porcentagem_btn = tk.Button(root, text='%', font=('Arial', 20), command=lambda: clique_butão("/100*"), bg='black',
                            fg='#FF85FF')
porcentagem_btn.grid(row=1, column=1, sticky='nsew')

apagar_btn = tk.Button(root, text='C', font=('Arial', 20), command=apagar, fg='black', bg="#FF6363")
apagar_btn.grid(row=1, column=0, sticky='nsew')

valor_btn = tk.Button(root, text="=", font=("Arial", 20), command=calcular, bg='#E26EE5', fg='white')
valor_btn.grid(row=5, column=3, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()