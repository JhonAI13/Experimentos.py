from random import sample

# Caracteres usados para formar
caracteres = 'abcdefghijklmnopqrstuvwxyz' \
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
             '0123456789' \
             '#@$%&*-=+/.'

# Tamanho da senha
tamanho = 30

# Gera senha
senha = "".join(sample(caracteres, tamanho))

# Mostrar resultados
print(senha)
