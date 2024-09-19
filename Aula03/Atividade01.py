# Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo


import os
os.system ("cls")
    
    # Com elif:

# valor = float (input (" Digite um valor "))
# if valor > 0:
#     print (" O valor é positivo")

# elif valor == 0:
#         print (" O valor 0 não é aceitável")

# else:
#     print (" O valor é negativo")



    # Sem elif:


# valor1 = float (input (" Digite um valor "))
# if valor1 != 0:
#     if valor1 > 0:
#         print (" O valor é positivo")
#     else:
#         print (" O valor é negativo")

# else:
#     print (" O valor 0 não é aceitável")
    
#################################################################################################################################

# Classificação IMC


# peso = float(input("Informe o peso em kg: "))
# altura = float(input("Informe a altura: "))
# imc = peso /(altura**2)

# if imc < 18.5:
#     print(f" Abaixo do peso. Seu IMC é {imc} ")

# elif  18.5 <= imc < 24.9  :
#     print(f" Peso normal. Seu IMC é {imc} ")

# elif  25.0 < imc < 29.9  :
#     print(f" Sobrepeso. Seu IMC é {imc} ")

# else:
#     print(f" Obesidade. Seu IMC é {imc} ")    


# OUTRA MANEIRA

# peso = float(input("Informe o peso em kg: "))
# altura = float(input("Informe a altura: "))
# imc = peso /(altura**2)

# if imc <= 18.5:
#      print(f" Abaixo do peso. Seu IMC é {imc} ")
# elif imc <= 24.9:
#     print(f" Peso normal. Seu IMC é {imc} ")

# elif imc <= 29.9:
#     print(f" Sobrepeso. Seu IMC é {imc} ")

# else:
#     print(f" Obesidade. Seu IMC é {imc} ")

#####################################################################################################################################



# profissao = input ("Profissão: ").upper()  # .upper() transforma o texto todo em maiúsculo
# localidade = input ("Localidadde: ").upper()

# if profissao  == "PROFESSOR" and localidade == "RIO DE JANEIRO":
#     print(" Tem desconto")
# else:
#     print (" Sem desconto")

resposta = input ('Quer desconto? ') [0].upper() # [0] pega a primeira letra (posição 0)
if resposta == 'S':
    print ("Tem desconto")
else:
    print ("Sem desconto")    