import re

def validacion_password(password):
    if len(password) < 8:
        return "Password inválido: debe tener al menos 8 caracteres."
    if not re.search("[A-Z]", password):
        return "Password inválido: debe tener al menos una letra mayúscula."
    if not re.search("[a-z]", password):
        return "Password inválido: debe tener al menos una letra minúscula."
    if not re.search("[0-9]", password):
        return "Password inválido: debe tener al menos un número."
    if not re.search("[^A-Za-z0-9]", password):
        return "Password inválido: debe tener al menos un carácter especial."
    return "Password válido."

# Ejemplos de entrada/salida
print(validacion_password("Contraseña123!"))  # Password válido
print(validacion_password("algo1!"))  # Password inválido: debe tener al menos 8 caracteres
print(validacion_password("minusculas123!"))  # Password inválido: debe tener al menos una letra mayúscula
print(validacion_password("MAYUSCULAS123!"))  # Password inválido: debe tener al menos una letra minúscula
print(validacion_password("SinNumeros!"))  # Password inválido: debe tener al menos un número
print(validacion_password("SinCaracteres123"))  # Password inválido: debe tener al menos un carácter especial
