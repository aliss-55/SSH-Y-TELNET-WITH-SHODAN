import os

def log_credenciales(ip, user, password, servicio="SSH"):
    os.makedirs("logs", exist_ok=True)
    with open("logs/valid_credentials.log", "a") as f:
        f.write(f"{servicio} -> {ip} - {user}:{password}\n")
