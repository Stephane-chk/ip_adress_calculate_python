from AdressTemplate import AddressTemplate
from Fonction import Fonction
class Ipv4 ( AddressTemplate ):
    def __init__(self,value_1,value_2,value_3,value_4):
        self.cidr = int()
        self.classes = ("A", "B", "C", "D", "E")
        AddressTemplate.__init__(self,value_1,value_2,value_3,value_4)
        self.isValidAddress()
        self.classe=None
        self.mask=None
        self.addressReseau=None
        self.addressDiffusion=None
        self.firstAddress=None
        self.lastAddress=None
        self.addressDispo=None
        pass

    def setCidr(self,x):
        result = self.parseInt(x)
        if result>30 or result<1:
            raise Exception('CIDR invalide')
        else:
            self.cidr = result
        pass

    def initData(self):
        if self.value_1>0 and self.value_1<127:
            self.classe = self.classes[0]
            self.initMaskAddress(self.getClass())
            self.initAddressReseau()
            self.initAddressDiffusion()
            self.initFirstAddress()
            self.initLastAddress()
            self.initAddressDispo()
        if self.value_1 > 127 and self.value_1 < 192:
            self.classe = self.classes[1]
            self.initMaskAddress(self.getClass())
            self.initAddressReseau()
            self.initAddressDiffusion()
            self.initFirstAddress()
            self.initLastAddress()
            self.initAddressDispo()
        if self.value_1 > 191 and self.value_1 < 224:
            self.classe = self.classes[2]
            self.initMaskAddress(self.getClass())
            self.initAddressReseau()
            self.initAddressDiffusion()
            self.initFirstAddress()
            self.initLastAddress()
            self.initAddressDispo()
        if self.value_1 > 223 and self.value_1 < 240:
            self.classe = self.classes[3]
        if self.value_1 > 239 and self.value_1 < 256:
            self.classe = self.classes[4]
        pass

    def initMaskAddress(self,classe):
        cidr = self.getCidr()
        if cidr == 0:
            if classe == 'A':
                self.mask = AddressTemplate(255,0,0,0)
            elif classe == 'B':
                self.mask = AddressTemplate(255,255,0,0)
            elif classe == 'C':
                self.mask = AddressTemplate(255,255,255,0)
        if cidr > 0:
            temp = AddressTemplate()
            reste = cidr;
            compteur = 0
            while(compteur<4):
                if reste>8:
                    reste = reste - 8
                    temp.appendValue(Fonction.generateDecimal(8))
                elif reste<8 and reste>0:
                    temp.appendValue(Fonction.generateDecimal(reste))
                    reste = 0
                elif reste==0:
                    temp.appendValue(Fonction.generateDecimal(0))
                    pass
                compteur += 1
                pass
            self.mask = temp



    def initAddressReseau(self):
        value1 = Fonction.logicalAND(self.getValue1(),self.getMask().getValue1())
        value2 = Fonction.logicalAND(self.getValue2() ,self.getMask().getValue2())
        value3 = Fonction.logicalAND(self.getValue3(),self.getMask().getValue3())
        value4 = Fonction.logicalAND(self.getValue4(),self.getMask().getValue4())
        value1 = Fonction.binaryToDecimal(value1)
        value2 = Fonction.binaryToDecimal(value2)
        value3 = Fonction.binaryToDecimal(value3)
        value4 = Fonction.binaryToDecimal(value4)
        self.addressReseau = AddressTemplate(value1,value2,value3,value4)
        pass

    def initAddressDiffusion(self):
        temp = self.getAddressReseau()
        diff = AddressTemplate()
        cidr = self.getCidr()
        compteur = 0
        reste = cidr
        if cidr==0 :
            temp = self.getAddressReseau()
            if self.getClass() == 'A':
                diff = AddressTemplate(temp.getValue1(),255,255,255)
            if self.getClass() == 'B':
                diff = AddressTemplate(temp.getValue1(), temp.getValue2(),255, 255)
            if self.getClass() == 'C':
                diff = AddressTemplate(temp.getValue1(), temp.getValue2(), temp.getValue3(), 255)
            pass
            self.addressDiffusion = diff
        if cidr>0 :
            while(compteur<4):
                if reste > 8:
                    reste = reste - 8
                    diff.appendValue(temp.getNextValue())
                elif reste < 8 and reste > 0:
                    toChange = Fonction.decimalToBinary(temp.getNextValue())
                    result = str(toChange)[0:reste]
                    toConcat=''
                    while(reste<8):
                        toConcat += '1'
                        reste += 1
                        pass
                    result = result +''+toConcat
                    diff.appendValue(Fonction.binaryToDecimal(result))
                    reste = 0
                elif reste == 0:
                    diff.appendValue(255)
                    pass
                compteur += 1
                pass
            self.addressDiffusion = diff
            pass

    def initFirstAddress(self):
        temp = self.getAddressReseau()
        value4 = (temp.getValue4())+1
        self.firstAddress = AddressTemplate(temp.getValue1(),temp.getValue2(),temp.getValue3(),value4)
        pass

    def initLastAddress(self):
        temp = self.getAddressDiffusion()
        value4 = temp.getValue4()-1
        self.lastAddress = AddressTemplate(temp.getValue1(),temp.getValue2(),temp.getValue3(),value4)
        pass

    def initAddressDispo(self):
        cidr = self.getCidr()
        if cidr == 0:
            if self.getClass() == 'A':
                self.addressDispo = (pow(2,32-(1*8)))-2
            elif self.getClass() == 'B':
                self.addressDispo = (pow(2,32-(2*8)))-2
            elif self.getClass() == 'C':
                self.addressDispo = (pow(2,32-(3*8)))-2
            pass
        if cidr > 0:
            self.addressDispo = (pow(2, 32 - cidr)) - 2
            pass

    def isValidAddress(self):
        if self.value_1<1 or self.value_1>255:
            if self.value_1==127:
                raise Exception("Addresse ip invalide")
            pass
        if self.value_4<1 or self.value_4>254:
            raise Exception("Addresse ip invalide")
        pass

    def getClass(self):
        return self.classe

    def getMask(self)->AddressTemplate:
        return self.mask

    def getAddressReseau(self)->AddressTemplate:
        return self.addressReseau

    def getAddressDiffusion(self)->AddressTemplate:
        return self.addressDiffusion

    def getFirstAddress(self)->AddressTemplate:
        return self.firstAddress

    def getLastAddress(self)->AddressTemplate:
        return self.lastAddress

    def getNbAddressDispo(self)->int:
        return self.addressDispo

    def getCidr(self)->int:
        return self.cidr