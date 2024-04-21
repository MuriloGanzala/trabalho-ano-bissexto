#Desenvolva um programa em Python que determine se um determinado ano é bissexto ou não, levando em consideração as regras do calendário gregoriano. 

# Primerio vamos solicitar ao usuário que insira o ano
ano = int(input("Digite o ano que você quer verificar: "))

# Verificar se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    bissexto = True
else:
    bissexto = False

# Imprimir resposta
if bissexto:
    print(f"O ano {ano} é bissexto e possui 366 dias.")
else:
    print(f"O ano {ano} não é bissexto e possui 365 dias.")

