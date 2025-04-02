class IP_ADDR():
    def __init__(self, ip: str | tuple[int, int, int, int]):
        if type(ip) == str:
            self.IP = tuple(ip.split("."))

        elif type(self.IP) == tuple:
            self.IP = ip

        self.IPValidator

    def IPValidator(self):
        if type(self.IP) == tuple:
            for i in range(len(self.IP)):
                if tuple[i] > 255 or tuple[i] < 0:
                    raise ValueError
        return 0

def nslookup(ip_range: list):
    operator = ip_range[0]

    if operator == 0:
        for ip in ip_range:
            pass # run nslookup
    
    elif operator == 1:
        start_addr = ip_range[1]
        end_addr = ip_range[2]
        

def run():
    #options = {0: }
    program = int(input("Enter Command: "))
