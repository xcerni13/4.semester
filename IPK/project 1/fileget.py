#VUT FIT Brno, Project 1 in IPK - client for file downloading
#Author: Rebeka Cernianska
#Login: xcerni13
#Date: 27.3.2021


import socket
import sys
import getopt
import time
import os

#loading and checking arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:")
except getopt.GetoptError:
    usage()

if (len(opts) != 2) or args:
    usage()

if (opts[0][0] == opts[1][0]):
    usage()

for i in opts:
    if(i[0] == "-n"):
        name_server = i[1]
    if(i[0] == "-f"):
        surl = i[1]

#formatting arguments to use as server name, ip address, port number
surl = surl.split("//")
details = surl[1].split("/")
server = details[0]
path = ""

#parsing path to file
if len(details) > 2:
    for i in (1,len(details)-1):
        if i > 1:
            path += "/"
        path += details[i]
else:
    path = details[1]


file_path = path.split("/")
file_name = file_path[len(file_path)-1]


if file_path[len(file_path)-1] == "index":
    file_name = "index"
    path = "index"

#parsing ip address and port number from arguments
ip_address, port = name_server.split(":")
initial_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#asking for server data
whereis_input = b"WHEREIS " + bytes(server, 'utf8')
#creating socket and receiving response from server
initial_socket.sendto(whereis_input, (str(ip_address), int(port)))
data, address = initial_socket.recvfrom(int(port))
initial_socket.close()
#checking connection response
resp = data.split(b" ")
if resp[0] != b"OK":
    print(data) #error printing
    exit(1)

tmp = data.split(b":")
data_port = int(tmp[1])


#downloading file data from server
def get_data(data_port, file_name):
    begin = time.time()
    timeout = 1
    finaldata = b''
    with open(file_name, "wb") as file:
        while True:
            data = file_data_socket.recv(data_port)
            if not data:
                if time.time() - begin > timeout:
                    break
            finaldata += (data)
        #parsing data from server into usable sections
        full_response = finaldata.split(b" ")
        response = full_response[1].split(b"\r\n")
        final = finaldata.split(b"\r\n\r\n")
        if (response[0] != b"Success"):
            print(final[1].decode('utf8'))
            file_data_socket.close()
            os.remove(file_name)
            exit(1)

        res = final[1]
        file.write(res)
        file.close()
    file_data_socket.close()
    return 0

#loading one file
if file_name != "*":
    file_data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_data_socket.connect((str(ip_address), data_port))
    file_data_socket.settimeout(2)

    get_input = b"GET " + bytes(path, 'utf8') + b" FSP/1.0\r\nHostname: " + bytes(server, 'utf8') + b"\r\nAgent: xcerni13\r\n\r\n"
    file_data_socket.sendall(get_input)

    finaldata = get_data(data_port, file_name)

    file_data_socket.close()
#loading multiple files
else:
    file_data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_data_socket.connect((str(ip_address), data_port))
    file_data_socket.settimeout(2)

    get_input = b"GET index FSP/1.0\r\nHostname: " + bytes(server, 'utf8') + b"\r\nAgent: xcerni13\r\n\r\n"
    file_data_socket.sendall(get_input)

    finaldata = b''

    while True:
        data = file_data_socket.recv(data_port)
        if not data:
            break
        finaldata += (data)

    full_response = finaldata.split(b" ")
    response = full_response[1].split(b"\r\n")

    if (response[0] != b"Success"):
        print("File not found")
        file_data_socket.close()
        os.remove(file_name)
        exit(1)

    final = finaldata.split(b"\r\n\r\n")
    res = final[1]

    files = res.split(b"\r\n")

    #downloading each file separately
    for current_file in range(len(files)-1):
        file_data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        file_data_socket.connect((str(ip_address), data_port))
        file_data_socket.settimeout(2)

        get_input = b"GET " + files[current_file] + b" FSP/1.0\r\nHostname: " + bytes(server, 'utf8') + b"\r\nAgent: xcerni13\r\n\r\n"
        file_data_socket.sendall(get_input)


        opts = files[current_file].split(b"/")
        file_name = opts[len(opts)-1]

        get_data(data_port, file_name)

        file_data_socket.close()
