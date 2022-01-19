import socket as s

# Host que deseja descobrir o Ip
host = 'instagram.com'

# Captura o Ip do Host desejado
Ip = s.gethostbyname(host)

# Mostra resultados
print(f'O IP do Host "' + host + '" é: ' + Ip)
