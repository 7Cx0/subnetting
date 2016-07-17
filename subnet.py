class Subnet:

    def __init__(self, ip_address, subnet_address):
        self.ip = ip_address
        self.sn = subnet_address
        self.na = [] #network address
        self.iplist = [int(x) for x in self.ip.split('.')]
        self.snlist = [int(y) for y in self.sn.split('.')]
        print(self.iplist)
        print(self.snlist)

    def flippedBinary(self,octet):
        octet=bytearray(octet)
        flipped = octet.translate(bytearray.maketrans(b'10',b'01'))
        return flipped

    def getNetworkAddress(self):
        for i in range(4):
            self.na.append(self.iplist[i] & self.snlist[i])
        return self.na

    def getBroadcastAddress(self):
        pass


a = Subnet('192.168.54.98', '255.255.255.248')
print(a.getNetworkAddress())
bitString = bytearray(b"11111000")
flippedString = bitString.translate(bytearray.maketrans(b'10',b'01'))
flippedString = (int(flippedString,base=2))
print(flippedString)
print(int(a.flippedBinary(b"11111000"),base=2))
