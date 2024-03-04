
import math

def calcular_metros_cubicos(alto, ancho, profundidad):
    metros_cubicos = alto * ancho * profundidad
    return metros_cubicos

def restar_ventanas_puertas(metros_cubicos, ventanas_puertas, profundidad):
    for ventana_puerta in ventanas_puertas:
        alto_ventana_puerta = float(input(f"    > Ingrese el alto de la {ventana_puerta} en centímetros: "))
        alto = alto_ventana_puerta/100
        ancho_ventana_puerta = float(input(f"    > Ingrese el ancho de la {ventana_puerta} en centímetros: "))
        ancho = ancho_ventana_puerta/100
        volumen_ventana_puerta = alto * ancho * profundidad
        metros_cubicos -= volumen_ventana_puerta
    return metros_cubicos

total_metros_cubicos = 0
operaciones = []

print()
print(">>>>>     CALCULADORA METROS CÚBICOS     <<<<<")
print()

while True:
    try:
        nombre_pared = input("Ingresa un nombre para la pared: ")
        print()
        alto = float(input("  - Ingresa la altura de la pared en metros: "))
        ancho = float(input("  - Ingresa el ancho de la pared en metros: "))
        profundidad_en_cm = float(input("  - Ingresa la profundidad de la pared en centímetros: "))
        profundidad = profundidad_en_cm / 100
        num_ventanas = int(input("  - Ingresa el número de ventanas: "))
        num_puertas = int(input("  - Ingresa el número de puertas: "))
        
        ventanas_puertas = [f"ventana {i + 1}" for i in range(num_ventanas)] + [f"puerta {i + 1}" for i in range(num_puertas)]

        metros_cubicos = calcular_metros_cubicos(alto, ancho, profundidad)
        metros_cubicos_restantes = round(restar_ventanas_puertas(metros_cubicos, ventanas_puertas, profundidad), 2)
        total_metros_cubicos += metros_cubicos_restantes
        total_metros = round(total_metros_cubicos, 2)
        total_metros_redondeados = math.ceil(total_metros)
        coste_total = total_metros_redondeados * 75  # Precio de bolas EPS es 75€ por metro cúbico
        operacion = {
            'nombre': nombre_pared,
            'metros_cubicos': metros_cubicos_restantes
        }
        operaciones.append(operacion)
        print()
        print(f"- Metros cúbicos de esta pared: {metros_cubicos_restantes} -")
        print()

        continuar = input("¿Deseas ingresar otra pared? (s/n): ").lower()
        print()
        print()

        if continuar != 's':
            break

    except ValueError:
        print()
        print("Por favor, ingresa únicamente números. En caso de ser números con decimales, estos debes indicarlos con un punto")
        print()

print("\nResumen de operaciones:")
print()

for operacion in operaciones:
    print(f"  - Pared '{operacion['nombre']}': {operacion['metros_cubicos']} metros cúbicos")

print(f"\n  >> Total de metros cúbicos de todas las paredes: {total_metros} metros <<")
print()
print()
finalizar = input("Para salir pulsa cualquier tecla > ")



Esta es la modificación que vamos a hacer. 
