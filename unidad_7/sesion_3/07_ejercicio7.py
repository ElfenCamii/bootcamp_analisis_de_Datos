###
# Ejercicio 7
# Inversión:
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.
###

user_invertion = float(input(': '))
user_fet = float(input('::'))
years = int(input(':::'))

for year in range(1, years + 1):
    capital_final = user_invertion * (1 + (user_fet/100))**year
    print(f'capital final año: {year} es de: {capital_final}')
