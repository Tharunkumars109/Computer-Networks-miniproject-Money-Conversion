from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Enter amount, from currency, to currency (e.g., 100 USD EUR): ')
    
    if message.lower() == 'exit':
        print("Exiting the currency converter.")
        break
    
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    response, serverAddress = clientSocket.recvfrom(2048)
    print(response.decode())

clientSocket.close()
