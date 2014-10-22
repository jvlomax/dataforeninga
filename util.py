import socket

def isOnline(ip):
    ports = [9, 20, 21, 22, 23, 80, 139, 1000, 443, 3389, 5500, 5800, 5900, 8080]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    for port in ports:
        try:
            s.connect((ip, port))
        except socket.error as e:
            s.close()
        else:
            return True
    return False
