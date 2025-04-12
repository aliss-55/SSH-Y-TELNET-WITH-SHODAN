import paramiko
from paramiko.ssh_exception import SSHException

def validate_ssh(ip, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=user, password=password, timeout=5)
        client.close()
        return True
    except SSHException as e:
        print(f"    ⚠️ SSHException en {ip}: {e}")
        return False
    except Exception as e:
        print(f"    ⚠️ Error general en {ip}: {e}")
        return False

