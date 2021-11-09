import ipaddress
class Ipv6 :
    def __init__(self):
        self.address = ''
        self.prefixe = 0
        self.address_reseau_compress = ''
        self.address_reseau_expand = ''
        pass

    def setAddress(self,ip):
        self.address = ip

    def getAddress(self):
        return  self.address

    def setPrefixe(self,p):
            self.prefixe = p

    def getPrefixe(self):
        return self.prefixe

    def displayAddressIpCompress(self):
        return str(ipaddress.IPv6Address(self.getAddress()).compressed)

    def displayAddressIpExpand(self):
        return str(ipaddress.IPv6Address(self.getAddress()).exploded)

    def getAddressReseauCompress(self):
        return self.address_reseau_compress

    def getAddressReseauExpand(self):
        return self.address_reseau_expand

    def initData(self):
        if ipaddress.IPv6Address(self.getAddress()):
            adress = ipaddress.IPv6Interface(self.getAddress()+'/'+str(self.getPrefixe()))
            self.address_reseau_compress =  str(adress.network.network_address.compressed)
            self.address_reseau_expand = str(adress.network.network_address.exploded)
        else:
            raise Exception('Ipv6 Invalide')




