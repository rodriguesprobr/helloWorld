minha_lista = ["biribá", "muruci", "cupuaçu", "bacuri"]

print(minha_lista)
print(minha_lista[0]) # Somente primeiro valor
print(minha_lista[:2]) # Somente os dois primeiros valores
print(minha_lista[2:]) # Somente depois do segundo valor
print(minha_lista[0:2]) # Somente os dois primeiros valores
print(minha_lista[:-1]) # Menos o último valor

minha_lista.append("uxi")
print(minha_lista)

minha_lista.sort()
print(minha_lista)

minha_lista.sort(reverse=True)
print(minha_lista)

valor_de_saida = minha_lista.pop()
print(minha_lista)
print(valor_de_saida)

# https://www.w3schools.com/python/python_ref_list.asp
