import string
import random

longitud = int(input(" Tamaño de la Contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña es: " + contraseña)

