import socket

def send_data(client, data_len_byte, data):
    if type(data) == str:
        data = data.encode()
    try:
      client.send(str(len(data)).zfill(data_len_byte).encode())
      client.send(data)
    except Exception as e:
        print(f"error in recv/send try again {str(e)}")


def layer1(msg):
    """
    the func add the text: "layer1" 10 times
    :param msg: text message
    :type: str
    :return: the new message
    :rtype": str
    """
    if type(msg) != str:
        msg = str(msg)

    msg += "layer1"*10
    return msg


def layer2(msg):
    """
    the func add the text: "-----" 10 times
    :param msg: text message
    :type: str
    :return: the new message
    :rtype": str
    """
    if type(msg) != str:
        msg = str(msg)
    msg += "-----" * 10
    return msg

def layer3(msg):
    """
    the func add the text: "1111111" 10 times
    :param msg: text message
    :type: str
    :return: the new message
    :rtype": str
    """
    if type(msg) != str:
        msg = str(msg)
    msg += "1111111" * 10
    return msg


def layer4(msg):
    """
    the func add the text: "HaHa" 10 times
    :param msg: text message
    :type: str
    :return: the new message
    :rtype": str
    """
    if type(msg) != str:
        msg = str(msg)
    msg += "HaHa" * 10
    return msg


def layer5(msg):
    """
    the func add the text: "last" 10 times
    :param msg: text message
    :type: str
    :return: the new message
    :rtype": str
    """
    if type(msg) != str:
        msg = str(msg)
    msg += "last" * 10
    return msg

my_sock = socket.socket()

menu = "enter text to send to server\nexit to finish: "

try:
    my_sock.connect(("127.0.0.1", 1455))

except Exception as e:
    my_sock.close()
    exit(f"server is down - try again {str(e)}" )

while True:

    msg_to_send = input(menu)


    if msg_to_send.lower() == 'exit':
        try:
            send_data(my_sock, 2, msg_to_send)
            break
        except Exception as e:
            break
    else:
        msg_to_send = layer1(msg_to_send)
        msg_to_send = layer2(msg_to_send)
        msg_to_send = layer3(msg_to_send)
        msg_to_send = layer4(msg_to_send)
        msg_to_send = layer5(msg_to_send)
        print(msg_to_send)
        try:
            send_data(my_sock, 3, msg_to_send)
        except Exception as e:
            print(f"error in recv/send - {str(e)}")
            break




print("by by")
my_sock.close()