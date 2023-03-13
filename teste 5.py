text = "Esse é um teste para vaga de Estágio"
inverso = "  "
for i in range(len(text)-1, -1, -2):
    inverso += text[i]
print(inverso)
