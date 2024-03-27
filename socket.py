import socket

while True:
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor = input("\n URL (exemplo : www.google.com.br): ")

    #CONECTANDO SOCKET
    soquete.connect((servidor, 80))

    #REQUISIÇÃO
    requisicao = f"GET / HTTP/1.1\r\nHost: {servidor}\r\n\r\n"
    soquete.send(requisicao.encode())

    #RESOSTA
    resposta = soquete.recv(32)
    print(resposta.decode())

    soquete.close()

    continuar = input("\n Outra solicitação? (s/n): ")
    if continuar == 'n':
        break
