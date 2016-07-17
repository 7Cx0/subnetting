class Subnet:

    def __init__(self, ip_address, subnet_address):
        self.ip = ip_address
        self.sn = subnet_address
        self.na = [] #network address
        self.ba = [] #broadcast address
        self.iplist = [int(x) for x in self.ip.split('.')]
        self.snlist = [int(y) for y in self.sn.split('.')]

    def flippedBinary(self,octet):
        octet=bytearray(octet)
        flipped = octet.translate(bytearray.maketrans(b'10',b'01'))
        return flipped

    def getNetworkAddress(self):
        for i in range(4):
            self.na.append(self.iplist[i] & self.snlist[i])
        return self.na

    def getBroadcastAddress(self):
        for i in range(4):
            self.ba.append(int(bytearray(bin(self.snlist[i]).encode()).translate(bytearray.maketrans(b'10',b'01')).decode()[2:],base=2) + self.na[i])
        return self.ba
    def getNextNetwork(self):
        pass
    def getPrevNetwork(self):
        pass
    def getFirstHost(self):
        pass
    def getLastHost(self):
        pass
    def getSubnet(self):
        pass
    def getHosts(self):
        pass


a = Subnet('192.168.54.98', '255.255.255.248')
print(a.getNetworkAddress())
print(a.getBroadcastAddress())
