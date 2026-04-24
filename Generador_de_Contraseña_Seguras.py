import string
import secrets

longitud = int(input("Tamaño de la contraseña: "))

if longitud < 4:
    print("La longitud debe ser al menos 4")
    exit()

# Garantizar al menos un tipo de cada
password = [
    secrets.choice(string.ascii_lowercase),
    secrets.choice(string.ascii_uppercase),
    secrets.choice(string.digits),
    secrets.choice(string.punctuation)
]

# Rellenar el resto
caracteres = string.ascii_letters + string.digits + string.punctuation
password += [secrets.choice(caracteres) for _ in range(longitud - 4)]

# Mezclar
secrets.SystemRandom().shuffle(password)

contraseña = "".join(password)

print("La contraseña es:", contraseña)