#git link - https://github.com/harelnutman-collab/onionPRJ
import socket



def remove_layer5(msg):
    """
    the func remove "last" 10 times
    :param msg: message
    :type: str
    :return: new message
    :rtype str
    """

    clean_text = str(msg).replace("last", "")
    return clean_text


def remove_layer4(msg):
    """
    the func remove "last" 10 times
    :param msg: message
    :type: str
    :return: new message
    :rtype str
    """
    if type(msg) != str:
        msg = str(msg)
    clean_text = msg.replace("HaHa", "")
    return clean_text


def remove_layer3(msg):
    """
    the func remove "last" 10 times
    :param msg: message
    :type: str
    :return: new message
    :rtype str
    """
    if type(msg) != str:
        msg = str(msg)
    clean_text = msg.replace("1111111", "")
    return clean_text


def remove_layer2(msg):
    """
    the func remove "last" 10 times
    :param msg: message
    :type: str
    :return: new message
    :rtype str
    """
    if type(msg) != str:
        msg = str(msg)
    clean_text = msg.replace("-----", "")
    return clean_text


def remove_layer1(msg):
    """
    the func remove "last" 10 times
    :param msg: message
    :type: str
    :return: new message
    :rtype str
    """
    if type(msg) != str:
        msg = str(msg)
    clean_text = msg.replace("layer1", "")
    return clean_text


server_sock = socket.socket()
server_sock.bind(("0.0.0.0", 1455))
server_sock.listen(3)

while True:
    client_sock, addr = server_sock.accept()

    print(f"{addr[0]} - connected")
    # handle the client
    while True:
        try:
            msg_len = int(client_sock.recv(3).decode())
            msg_data = str(client_sock.recv(msg_len).decode())
        except Exception as e:
            print(f"error in recv/send - {str(e)}")
            break

        if msg_data.lower() == "exit":
            break

        msg_data = remove_layer5(msg_data)
        msg_data = remove_layer4(msg_data)
        msg_data = remove_layer3(msg_data)
        msg_data = remove_layer2(msg_data)
        msg_data = remove_layer1(msg_data)

        print(msg_data)

    print(f"{addr[0]} - disconnected")
    client_sock.close()










