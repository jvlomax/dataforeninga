
import socket


def isOnline(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((ip, 22)) #ssh

    except socket.error as e:
        pass
    else:
        return True

    try:
        s.connect((ip, 80)) # http
    except socket.error as e:
        pass
    else:
        return True

    try:
        s.connect((ip, 10000)) #webmin
    except socket.error as e:
        pass
    else:
        return True
    return False