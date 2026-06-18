# Tratamento de Erros
# Erros comuns:
# - SyntaxError: Erro de sintaxe, geralmente causado por erros de digitação ou estrutura incorreta do código.
# - NameError: Ocorre quando uma variável ou função é referenciada antes de ser definida. 
# - TypeError: Acontece quando uma operação é aplicada a um tipo de dado inadequado.

# Exemplo de tratamento de erros usando try-except
# def dividir(a, b):
#     try:
#         resultado = a / b
#         print(f"O resultado da divisão é: {resultado}")
#     except ZeroDivisionError:
#         print("Erro: Não é possível dividir por zero.")
#     except TypeError:
#         print("Erro: Os valores devem ser números.")
#     except Exception as e:
#         print(f"Ocorreu um erro inesperado: {e}")

# dividir(10, 2)  # Saída: O resultado da divisão é: 5.0
# dividir(10, 0)  # Saída: Erro: Não é possível dividir por zero.
# dividir(10, "a")  # Saída: Erro: Os valores devem ser números.

# 1
import tkinter as tk
from tkinter import messagebox

# 5
def dividir():
    number1 = int(ent_number1.get())
    number2 = int(ent_number2.get())
    try:
        if number1 == 0 and number2 == 0:
            messagebox.showwarning("Verificar", "Inserir valores diferentes de 0")
        calculo_divisao = number1 / number2
        messagebox.showinfo("Resultado", f"Resultado divisão: {calculo_divisao}")
    except ZeroDivisionError:
        print('Erro: Não é possível dividir por zero.')
    except NameError:
            messagebox.showerror("Erro", "Inserir numeros")
    except ValueError:
            messagebox.showerror("Erro", "Inserir numeros válidos")

# 2
janela = tk.Tk()
janela.title("Tratamento de Erros")
janela.geometry("500x400")
janela.configure(bg="grey")

# 3
lbl_titulo_aplicacao = tk.Label(janela, text='Calculadora divisora :)', font=('Arial', 14),fg="black", bg="grey")
lbl_titulo_aplicacao.grid(row=0, column=0, padx=10, pady=10)
lbl_number1 = tk.Label(janela, text="Digite o primeiro valor: ", font=("Arial", 12), fg="black", bg="grey")
lbl_number1.grid(row=1, column=0, padx=10, pady=10)
lbl_number2 = tk.Label(janela, text="Digite o segundo valor: ", font=("Arial", 12), fg="black", bg="grey")
lbl_number2.grid(row=2, column=0, padx=10, pady=10)
# lbl_number1.pack() - Centraliza conteúdo na tela

# 4
ent_number1 = tk.Entry(janela, font=("Arial", 12))
ent_number1.grid(row=1, column=1, padx=10, pady=10)
ent_number2 = tk.Entry(janela, font=("Arial", 12))
ent_number2.grid(row=2, column=1, padx=10, pady=10)

# 6
btn_dividir = tk.Button(janela, text="Dividir", font=("Arial", 12), width=15, height=2, bg='light grey' , command=dividir)
btn_dividir.grid(row=3, column=0, pady=10, padx=10)
btn_fechar = tk.Button(janela, text="Fechar aplicativo", font=("Arial", 12), width=15, height=2, bg='light grey', command=janela.destroy)
btn_fechar.grid(row=3, column=1, pady=10, padx=10)

# 7
janela.mainloop()