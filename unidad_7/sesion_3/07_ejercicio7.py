###
# Ejercicio 7
# Inversión:
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.
###

user_invertion = float(input(': '))
user_fet = float(input('::'))
years = float(input(':::'))

capital_final = user_invertion * (1 + (user_fet/100))**years

print(capital_final)