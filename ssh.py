import paramiko
from paramiko.ssh_exception import SSHException
import socket

def validate_ssh(ip, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=user, password=password, timeout=5)
        client.close()
        return True
    except SSHException as e:
        print(f"    ⚠️ SSH error en {ip}: {str(e).split(':')[0]}")
        return False
    except socket.error as e:
        print(f"    ⚠️ Socket error en {ip}: {e}")
        return False
    except Exception:
        print(f"    ⚠️ Fallo desconocido en {ip}")
        return False
