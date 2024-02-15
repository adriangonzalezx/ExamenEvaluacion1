def descomponer_ip(ip):
    octetos = ip.split('.')
    for octeto in octetos:
        print(octeto)

# Ejemplo de uso
ip = "192.168.1.1"
descomponer_ip(ip)
