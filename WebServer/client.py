from socket import *
import sys

if len(sys.argv) != 4:
    print(f'Invalid arguments, should be in format: {__file__} server_host server_port filename')
    sys.exit()

serverHost = sys.argv[1]
serverPort = sys.argv[2]
filename = sys.argv[3]
result = ''

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, int(serverPort)))

clientSocket.send(f'GET /{filename} HTTP/1.1\r\nHost: {serverHost}:{serverPort}\r\nConnection: keep-alive\r\nAccept: text/html'.encode())
print(f"http://{serverHost}:{serverPort}/{filename}")

currentResult = ' '
while currentResult:
    currentResult = clientSocket.recv(1024)
    result += currentResult.decode()

print(result)

clientSocket.close()
