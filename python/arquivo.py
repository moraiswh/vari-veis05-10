# 1 - Crie uma variável mnsagem e exiba uma mensagem na tela
# 2 - Crie uma variável número e exiba esse número na tela
# 3 - Crie duas variáveis númericas e faça as 4 operações matemáticas
# com esses números. Faça também a exponenciação e o resto da divisão
# 4 - Crie duas variáveis de texto e faça a concatenação dessas
# mensagens
# 5 Faça um programa que receba um texto e faça repetir 5 vezes
# 6 - Crie uma variável de texto em minúsculo e deixe-o com todas as letras maiúsculas 
# 7 - Crie um programa que recebe um texto do usuário e exiba na tela 
# * Crie um programa que receba o usuário, nome , idade, altura, cidade e estado e exiba a seguinte frase na tela "olá, meu nome é_____, tenho _____ anos de idade, moro na cidade ______/___".
# 9 - Crie um programa com uma variável número qualquer; Depois, crie uma variável chute pedindo para o usuário digitar um número. Na sequência, crie uma condição para saber se o chute é igual a variável. Caso seja igual exiba uma mnensagem "você acertou", se for diferente exiba a mensagem "você errou" 


mensagem = 'Olá Mundo'
print (mensagem)

numero1 = 10
print (numero1)

numero3 = 20
numero4 = 30 
soma = numero3 + numero4
sub = numero4 - numero3
div = numero3 / numero4
multi = numero3 * numero4 
print (soma)
print (sub)
print (div)
print (multi)

expo = numero3 ** numero4
resto_diva = numero4 % numero3
divi_inteira = numero4 // numero3
print (expo)
print (resto_diva)
print (divi_inteira)

texto1 = "batata"
texto2 = "banana"
c = texto1 + " " + texto2
print(c)

text = "aula"
repeticao = text * 5
print (repeticao)

text2 = "bom dia"
#text2.upper()
print(text2.upper())

texto = input("Coloque sua mensagem")
print(texto)

nome2 = input ("Pedro") 
idade = int (input("16"))
altura = float (input("1,83"))
cidade = input("Maringá")
estado = input ("Paraná")

print ('meu nome é {nome2}, tenho {idade} anos de idade, altura {altura}, moro na cidade de {cidade} no estado de {estado}')