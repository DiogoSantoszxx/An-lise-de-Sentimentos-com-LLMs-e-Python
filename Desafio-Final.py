#etapa 1 // carregar um arquivo .txt onde cada linha será um elemento de uma lista python
lista_resenha = []

with open("resenhas-chat-LLM.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_resenha.append(linha.strip())
        
        
print(lista_resenha)

#etapa 2 //

for resenha in lista_resenha:
    