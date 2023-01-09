import calculadora

def main():
    
    while True:
        try:
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            break
        except ValueError:
            print("Por favor, Ingrese un numero valido")
    
    
    while True:
        operacion = input("Indique operacion a realizar: ").lower()
        if operacion == "suma":
            resultado = calculadora.suma(n1,n2)
            break
        elif operacion == "resta":
            resultado = calculadora.resta(n1,n2)
            break
        elif operacion == "multiplicacion":
            resultado = calculadora.multiplicacion(n1,n2)
            break
        elif operacion == "division":
            resultado = calculadora.division(n1,n2)
            break
        else:
            print("Por favor ingrese una operacion valida!!!")
        
    print("El resultado es: " + str(resultado))
    
if __name__ == "__main__":
    main()
