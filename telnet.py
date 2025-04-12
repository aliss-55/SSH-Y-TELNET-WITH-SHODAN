import telnetlib

def validate_telnet(ip, user, password):
    try:
        tn = telnetlib.Telnet(ip, timeout=5)
        tn.read_until(b"login: ", timeout=5)
        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password: ", timeout=5)
        tn.write(password.encode('ascii') + b"\n")
        salida = tn.read_some().decode('ascii')
        tn.close()
        if "incorrect" not in salida.lower():
            return True
        return False
    except:
        return False
