#!/usr/bin/env python3

import socket

# hard coded objects to fix later
out_file_path = "/home/diamo/Programs/output/part-c-out.txt"
out_file = open(out_file_path, "w")


class IP_ADDR():
    def __init__(self, ip: str | tuple[int, int, int, int]):
        if type(ip) == str:
            self.IP = list(ip.split("."))

        elif type(ip) == list:
            self.IP = ip

        else:
            raise TypeError

        self.IPValidator()
        self.intCast(self.IP)

    def intCast(self, data: list | tuple | set):
        for i in range(len(data)):
            data[i] = int(data[i])

    def humanReadable(self):
        data = ""
        for octet in self.IP:
            data += str(octet)+"."
        return data[:-1]

    def IPValidator(self):
        if type(self.IP) == list:
            for i in range(len(self.IP)):
                if int(self.IP[i]) > 255 or int(self.IP[i]) < 0:
                    raise ValueError(f"Octet {i} is out of range. must be between 0-255")
            if len(self.IP) != 4:
                raise IndexError("Insufficent number of octets in IP")
        return 0

def IPEnumeration(start_addr: IP_ADDR, end_addr: IP_ADDR, params):
    # add warnings about doing a large number of addresses, > 65025
    if type(params) != list:
        params = list(params)

    if params.count("v") >= 1:
        print("Verbose mode selected")

    OCT1 = None
    OCT2 = None
    OCT3 = None
    if start_addr.IP[0] == end_addr.IP[0]:
        OCT1 = start_addr.IP[0]

    if start_addr.IP[1] == end_addr.IP[1] and OCT1:
        OCT2 = start_addr.IP[1]
    
    if start_addr.IP[2] == end_addr.IP[2] and OCT2:
        OCT3 = start_addr.IP[2]

    if start_addr.IP[3] == end_addr.IP[3] and OCT3:
        raise TypeError("IP addresses match - change mode of operation or change IP addresses provided")
    
    current_addr = IP_ADDR(start_addr.IP)

    while current_addr.IP != end_addr.IP:
        current_addr.IP[3] += 1
        if current_addr.IP[3] == 256:
            current_addr.IP[2] += 1
            current_addr.IP[3] = 0
        
        if current_addr.IP[2] == 256:
            current_addr.IP[1] += 1
            current_addr.IP[2] = 0
        
        if current_addr.IP[1] == 256:
            current_addr.IP[0] += 1
            current_addr.IP[1] = 0  
        try:
            ip_resolve = socket.gethostbyaddr(current_addr.humanReadable())
        except socket.herror:
            ip_resolve = ["Unknown / Unresolvable host"]


        output = f"IP: {current_addr.humanReadable()} | NSLOOKUP: {ip_resolve[0]}"
        out_file.write(output + "\n")

        if params.count("v") >= 1:
            print(output)
    
        

def run():
    ip1 = input("Enter start IP addr: ")
    ip2 = input("Enter end IP addr: ")
    params = input("Enter parameters: ")
    IPEnumeration(IP_ADDR(ip1), IP_ADDR(ip2), params)
    
run()