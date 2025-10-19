# Criando um dicionario de exemplo
pessoa = {"nome": "Carlos", "idade": 30, "cidade": "São paulo"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva" # Criando chaves mesmo após o dicionário ja ter sido criado
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31 # Mudando a idade mesmo após o dicionário ter sido criado
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()

#keys()
chaves = list(pessoa.keys()) # Usar o List para tranformar o dicionário em lista 
print("Chaves do dicionário:", chaves) # Mostra todas as chaves
print("Primeira chave:", chaves[0]) # Mostra a chave do indice indicado

#values()
valores = list(pessoa.values()) # Usar o List para tranformar o dicionário em lista 
print("Valores do dicionário:", valores) # Mostra todos os valores
print("Primeiro valor do dicionário:", valores[0]) # Mostra o valor do indice indicado

# Método items
itens = pessoa.items() # Usar o List para tranformar o dicionário em lista 
print ("Pares chave-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0] [0], itens[0] [1]))
