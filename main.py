import tkinter as tk
import qrcode as qr

def executar_programa():
    textoDados = textoAluno.get("1.0","end-1c")
    ##textoImagem = textoPng.get("1.0", "end-1c")
    img = qr.make(textoDados)
    type(img)
    img.save(textoDados + ".png")

janela = tk.Tk()
alunoNome = tk.Label(janela, text="Digite o nome do Aluno: ")
alunoNome.pack()

textoAluno = tk.Text(janela, width=40, height=5)
textoAluno.pack()

##png = tk.Label(janela, text="Digite o nome do arquivo: ")
##png.pack()

##textoPng = tk.Text(janela, width=40, height=5)
##textoPng.pack()

botao = tk.Button(janela, text="Gerar o QRCode", command=executar_programa)
botao.pack()

janela.mainloop()