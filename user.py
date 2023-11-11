import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.23.21.223', 16789))


while True:
    key_input = input("Нажмите Enter")
    if key_input == '':
        client_socket.send(b'button_pressed')
