import socket
from _thread import *

HOST = '127.0.0.1'
PORT = 9999
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리

def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024)
        print(data.decode())

start_new_thread(recv_data, (client_socket,))

userName=str(input("사용자 이름 : "))
client_socket.send(userName.encode())

print ('채팅방에 입장합니다')

while True:
    message = input()
    client_socket.send(message.encode())
    if message == 'quit':
        print("채팅방에서 퇴장하셨습니다")
        break

client_socket.close()