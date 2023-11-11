import socket
from _thread import *
from changeWord import *
from whisper import *
from p2pchat import *

#접속자 목록
c_list = []

#클라이언트들 간의 연결 저장
c_connections={}


def groupChat(c_socket, addr):
    sender_info = f"{addr[0]}:{addr[1]}"  #발신자 정보
    print(f">> {sender_info} 님이 입장하셨습니다.")
    
    while True:
        try:
            data = c_socket.recv(1024).decode('utf-8')
            sendTime, recvMessage = data.split(' ', 1)    #받은 메시지, 보낸 시간 분리
            
            if not data:
                print(f">> {sender_info} 님이 대화방을 나갔습니다.")
                break
            
            #귓속말 기능
            print(f"testrecvmessage : {recvMessage}")
            if recvMessage.startswith('/w'):
                whisper(recvMessage)

            #1:1 대화 기능
            elif recvMessage.startswith('/p'):
                p2pchat(recvMessage)

            #1:1 요청 받으면
            elif c_socket in c_connections:
                recipient_socket=c_connections[c_socket]

                if recvMessage.lower()=='y':
                    recipient_socket=c_connections[c_socket]
                    c_socket.send(f"1:1 대화가 수락되었습니다.".encode())
                    recipient_socket.send(f"1:1 대화가 수락되었습니다.".encode())
                elif recvMessage.lower()=='n':
                    c_socket.send(f"1:1 대화 요청이 거부되었습니다.".encode())
                    recipient_socket.send(f"1:1 대화 요청이 거부되었습니다.".encode())
                    del c_connections[c_socket]
                else:
                    recipient_socket.send(f"{addr[1]}: {recvMessage}".encode())

            #일반 채팅
            else:
                filtered_data = changeWord(recvMessage)
                print(f"{sender_info} - {recvMessage}  {sendTime}")  #오가는 메시지들 로깅
                
                for client in c_list:
                    if client != c_socket:
                        client.send(filtered_data.encode('utf-8'))
                    
        except ConnectionResetError as e:
            print(f">> {sender_info} 님이 대화방을 나갔습니다.")
            for client in c_list:
                if client != c_socket:
                    client.send(f">> {sender_info} 님이 대화방을 나갔습니다.".encode('utf-8'))
            break
                            
    if c_socket in c_list:
        c_list.remove(c_socket)
        print('>> 접속자 목록을 갱신했습니다 - 접속자 수 : ', len(c_list))
        print(c_list)
        
    c_socket.close()


def start_server():
    PORT = 12346
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind(('', PORT))
    s_socket.listen()

    print('>> 012 Chat Server Start')
    print('>> 접속자를 기다리는 중...\n')

    try:
        while True:
            c_socket, addr = s_socket.accept()
            c_list.append(c_socket)
            print("접속자 수 : ", len(c_list))
            start_new_thread(groupChat, (c_socket, addr))

    except Exception as e:
        print('에러 발생:', e)
    finally:
        s_socket.close()


if __name__ == "__main__":
    start_server()
