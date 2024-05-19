def obtener_datos_usuario():
    nombre = input("Introduce tu nombre: ").strip()
    apellido_paterno = input("Introduce tu apellido paterno: ").strip()
    apellido_materno = input("Introduce tu apellido materno: ").strip()
    
    while True:
        try:
            edad = int(input("Introduce tu edad: ").strip())
            if edad <= 0:
                raise ValueError("La edad debe ser un número positivo.")
            break
        except ValueError as e:
            print("Error: La edad debe ser un número entero positivo.")
    
    while True:
        try:
            peso = float(input("Introduce tu peso en kilogramos: ").strip())
            if peso <= 0:
                raise ValueError("El peso debe ser un número positivo.")
            break
        except ValueError as e:
            print("Error: El peso debe ser un número positivo.")
    
    while True:
        try:
            estatura = float(input("Introduce tu estatura en metros: ").strip())
            if estatura <= 0:
                raise ValueError("La estatura debe ser un número positivo.")
            break
        except ValueError as e:
            print("Error: La estatura debe ser un número positivo.")
    
    return nombre, apellido_paterno, apellido_materno, edad, peso, estatura

def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

def mostrar_datos(nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc):
    print("\n--- Datos del Usuario ---")
    print(f"Nombre: {nombre}")
    print(f"Apellido Paterno: {apellido_paterno}")
    print(f"Apellido Materno: {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")

nombre, apellido_paterno, apellido_materno, edad, peso, estatura = obtener_datos_usuario()
imc = calcular_imc(peso, estatura)
mostrar_datos(nombre, apellido_paterno, apellido_materno, edad, peso, estatura, imc)
