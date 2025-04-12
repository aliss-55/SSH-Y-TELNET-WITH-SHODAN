import os

# Ruta exacta al archivo que tú tienes
ruta_users = "D:/Users/Alisson/Desktop/telnet/credentials/users.txt"
ruta_passwords = "D:/Users/Alisson/Desktop/telnet/credentials/passwords.txt"

# 1. Verificar si el archivo existe
print("[+] Verificando existencia de archivos...")
print("¿Users existe?", os.path.exists(ruta_users))
print("¿Passwords existe?", os.path.exists(ruta_passwords))

# 2. Intentar abrir y leer
try:
    with open(ruta_users, 'r', encoding='utf-8') as f:
        users = f.read().splitlines()
    print(f"[OK] Usuarios cargados ({len(users)}): {users}")
except Exception as e:
    print(f"[ERROR] Falló al leer users.txt: {e}")

try:
    with open(ruta_passwords, 'r', encoding='utf-8') as f:
        passwords = f.read().splitlines()
    print(f"[OK] Passwords cargados ({len(passwords)}): {passwords}")
except Exception as e:
    print(f"[ERROR] Falló al leer passwords.txt: {e}")
