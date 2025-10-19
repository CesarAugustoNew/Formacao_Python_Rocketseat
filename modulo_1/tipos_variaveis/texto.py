#Declaração
nome_completo = "Cesar Augusto"

nome_completo_aspas = """Cesar
Augusto"""

nome_completo_quebra = "Cesar \
Augusto"

nome = "Cesar"
sobrenome = "Augusto"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Cesar" + "Augusto")
print("Nome completo (4a forma):" + "Cesar", "Augusto")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))

nome.upper() # Deixa a string em maiuscula
nome.lower() # Deixa a string em minuscula
nome[0] # Para acessar a primeira letra
nome_completo.count("a") # Conta quantas vezes tem a letra A
nome_completo.find("a") # Mostra a posição da letra A
nome.encode() # Converter uma string em uma sequência de bytes
nome.encode().decode() # Converte os bytes em string
nome_completo.replace("c", "a") #Substitui todas as letras C por letra A
"-".join("Cesar") # Separa cada caracter por -
nome_completo.split(" ") # Divide a string em uma lista com base em um caracter alvo 
nome.strip("x") # Remove tudo que ta no comeco e no final que corresponde com o alvo
nome.rstrip("x") # Remove so o da direita
nome_completo.startswith("ce") # Compara pra saber se o nome começa com uma determinada string ou não
"ce" in nome_completo # Compara se existe ce na variavel nome_completo (Resultado True)
"abc" not in nome_completo # Compara se abc existe no nome completo (Resultado False)
