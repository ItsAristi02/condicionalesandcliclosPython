
nivelAgua = int(input("Cúal es el nivel del agua: "))

if nivelAgua > 0 and nivelAgua <= 200:
    print(f"El nivel de agua es: {nivelAgua}, por lo que esta muy bajo")
elif nivelAgua > 200 and nivelAgua <= 400:
    print(f"El nivel de agua es: {nivelAgua}, por lo que se esta operando con normalidad")
elif nivelAgua > 400:
    print(f"El nivel de agua es: {nivelAgua}, inicie plan de evacuación!!!!")
else:
    print("Por favor revise el sensor, nivel no valido")