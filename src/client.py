import socket
import time
from _thread import *

#서버 데이터 받기
def receive(c_socket, window, callback):
    global nickname, datetime
    while True:
        try:
            recvData = c_socket.recv(1024)
            if not recvData:
                print("연결이 종료되었습니다.")
                break
            decoded_data = recvData.decode('utf-8')
            if decoded_data == "NICKNAMECHANGE::FALSE":
                print("실패")
                change_nick(window,1)
            elif decoded_data == "NICKNAMECHANGE::TRUE":
                print("성공")
                change_nick(window,0)

            display_text = ""
            if '**' in decoded_data:
                nickname, datetime, data = decoded_data.split('**', 2)
                display_text = f"{nickname}  {datetime}\n{data}"
                callback(display_text)

        except Exception as e:
            print(f"예외가 발생했습니다: {e}")
            break

# 서버 연결
def connect_to_server(window, callback):
    global c_socket
    HOST = "127.0.0.1"
    PORT = 12346

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((HOST, PORT))

    start_new_thread(receive, (c_socket, window, callback))

def my_portNum():
    return str(c_socket.getsockname()[1])

def changing_nickname(new):
    global tmp
    tmp = new
    c_socket.send(("NICKNAMECHANGE::"+tmp).encode('utf8')) #행동+닉네임

def change_nick(window,flag):
    global tmp
    print(tmp)
    if flag:
        tmp += window.port
        c_socket.send(("NICKNAMECHANGE::"+tmp).encode('utf8'))
    if window.Text_myName:
        window.nickname = tmp
        window.Text_myName.setText(window.nickname)
    else:
        window.nickname = tmp

#메시지, 입력 시간 보내기
def send_message(message):
    sendTime = time.strftime('%Y/%m/%d %H:%M:%S')  # 입력시간
    c_socket.send((f'{sendTime}**{message}').encode('utf-8'))

#서버 연결 종료
def close_connection():
    try:
        c_socket.close()
    except Exception as e:
        print(f"서버 연결 종료 중 오류 발생: {e}")
