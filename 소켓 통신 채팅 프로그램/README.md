# 소켓 통신 채팅 프로그램

<br>

## TCP 방식으로 구현
IP주소를 사용하여 패킷으로 변환된 데이터를 전달

### 서버 소켓

1. socket() : 소켓 생성
2. bind() : IP주소와 소켓을 바인딩
    - int bind(SOCKET sockfd, const sockaddr *my_addr, int namelen);
    - sockfd : 앞서 socket 함수로 생성된 endpoint 소켓의 식별 번호
    - my_addr : IP 주소와 port 번호를 저장하기 위한 변수가 있는 구조체
    - namelen : sockfd의 데이터 크기
    - return : 성공 시 0, 실패 시 -1

3. listen() : 소켓 가동, 클라이언트의 소켓 기다리기
4. accept() : 클라이언트와 연결
5. send()/recv() : 데이터 송수신
6. close() : 소켓 종료

## 클라이언트 소켓

1. socket() : 소켓 생성
2. connect() : 서버 소켓에 연결 시도
3. send()/recv() : 데이터 송수신
4. close() : 소켓 종료

## 실행화면
![image](https://github.com/nunomi0/network/assets/109198538/f694bd0f-4ea5-4dfe-a9d3-577158d6b0ea)


- HOST = 127.0.0.1
- 자기 자신의 IP 주소로 연결하도록 설정하여 같은 컴퓨터 내에서 채팅할 수 있도록 하였다.
ifconfig(Ipconfig) 명령어를 통해 자신의 IP 주소를 알아낸 후, server IP 주소로 지정하여 채팅할 수 있도록 하였다.
- 'ping IP주소' 명령어를 통해 해당 IP주소에 연결이 가능한지 확인할 수 있다.
- 리눅스와 윈도우 간에 IP 연결이 되지 않았다. 인바운드 규칙, 아웃바운드 규칙을 설정해 주어야 한다.


