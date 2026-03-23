import random
from faker import Faker


fake = Faker("es_ES")

def generar_datos_validos():
    return {
        "nombre": fake.name(),
        "cedula": generar_cedula_ecuatoriana(),
        "telefono": generar_telefono(),
        "email": fake.email()
    }

def generar_datos_invalidos():
    return {
        "nombre": "1234",
        "cedula": "000",
        "telefono": "abc",
        "email": "correo_invalido"
    }

def generar_datos_vacios():
    return {
        "nombre": "",
        "cedula": "",
        "telefono": "",
        "email": ""
    }
    
def generar_cedula_ecuatoriana():
    # 1. Provincia válida (01–24)
    provincia = random.randint(1, 24)
    provincia_str = str(provincia).zfill(2)

    # 2. Tercer dígito (0–5)
    tercer_digito = str(random.randint(0, 5))

    # 3. Generar los siguientes 6 dígitos
    restantes = [str(random.randint(0, 9)) for _ in range(6)]

    # Primeros 9 dígitos
    cedula_base = list(provincia_str + tercer_digito + "".join(restantes))

    # 4. Calcular dígito verificador
    suma = 0
    for i in range(9):
        num = int(cedula_base[i])
        if i % 2 == 0:  # posiciones pares (0-based)
            num *= 2
            if num > 9:
                num -= 9
        suma += num

    decena = ((suma + 9) // 10) * 10
    digito_verificador = decena - suma if decena - suma != 10 else 0

    cedula = "".join(cedula_base) + str(digito_verificador)

    return cedula

def generar_telefono():
    return "09" + str(random.randint(10000000, 99999999))