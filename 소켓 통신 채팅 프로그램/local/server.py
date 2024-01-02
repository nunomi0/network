import socket
from _thread import *

client_sockets = [] # 서버에 접속한 클라이언트 목록
client_names={}

# 쓰레드에서 실행되는 코드
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신

# 서버 IP 및 열어줄 포트
HOST = '127.0.0.1'
PORT = 9999

# 서버 소켓 생성

# socket.AF_INET : IPv4 인터넷 프로토콜 사용
# socket.SOCK_STREAM : TCP 연결 기반, 신뢰성 있고 순서대로 전송
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.SOL_SOCKET : 소켓 옵션 설정
# socket.SO_REUSEADDR : 소켓을 닫은 후에도 주소(포트) 재사용 가능
# 1 : SO_REUSEADDR 옵션 활성화
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 소켓에 IP와 포트를 할당
server_socket.bind((HOST, PORT))

# 클라이언트 연결 요청 받을 준비
server_socket.listen()

print('서버를 열었습니다')
def send_to_all(message,sender_socket=None):
  for client in client_sockets:
    if client!=sender_socket:
      client.send(message.encode())
      
def threaded(client_socket, addr):
    name = client_socket.recv(1024).decode()
    client_names[client_socket]=name
    serverMessage=f"{name}({addr[0]}/{addr[1]})님이 입장하였습니다"
    print(serverMessage)
    send_to_all(serverMessage)

    # 클라이언트가 접속을 끊을 때 까지 반복
    while True:
        try:
            data=client_socket.recv(1024).decode()
            
            if (not data or data=="quit"):
              break
            
            # 데이터가 수신되면 클라이언트에 다시 전송
            fullMessage=f"{name} : {data}"
            print(fullMessage)

            # 서버에 접속한 클라이언트들에게 채팅 보내기
            # 메세지를 보낸 본인을 제외한 서버에 접속한 클라이언트에게 메세지 보내기
            for client in client_sockets : # 연결된 주소들 중에서
                if client != client_socket : # 자기자신이 아닌 경우
                    client.send(fullMessage.encode())
                    
        except ConnectionResetError as e:
            break

    if client_socket in client_sockets :
        client_sockets.remove(client_socket)
        del client_names[client_socket]
        serverMessage=f"{name}({addr[0]}/{addr[1]})님이 퇴장하였습니다"
        send_to_all(serverMessage)
        print(serverMessage)

    client_socket.close()


# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴
# 새로운 쓰레드에서 해당 소켓을 사용하여 통신
try:
    while True:
        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수 : ", len(client_sockets))

except Exception as e :
    print ('에러 : ',e)

finally:
    server_socket.close()
