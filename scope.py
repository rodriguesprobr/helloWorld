# escopo global
minha_string_global = "Eu sou uma variável global, posso ser acessada de qualquer função ou classe"

def acessar_variavel_global():
    print(minha_string_global)

#escopo local
def acessar_variavel_local():
    minha_string_local = "Eu sou uma variável local, só posso ser acessada dentro dessa função ou classe"
    print(minha_string_local)

acessar_variavel_global()

acessar_variavel_local()