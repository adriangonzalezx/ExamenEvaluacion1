def calcular_interes_compuesto():
    capital_inicial = 1000
    
    # Solicitar la tasa de interés
    while True:
        tasa_interes = float(input("Introduce la tasa de interés anual (entre 1% y 10%): "))
        if 1 <= tasa_interes <= 10:
            break
        else:
            print("La tasa de interés debe estar entre 1% y 10%. Intenta de nuevo.")
    
    # Solicitar el número de años
    años = int(input("Introduce el número de años: "))
    
    # Convertir la tasa de interés a decimal
    tasa_interes /= 100
    
    # Calcular el capital final
    capital_final = capital_inicial * (1 + tasa_interes) ** años
    
    print(f"El capital final después de {años} años es: {capital_final:.2f}")

calcular_interes_compuesto()
