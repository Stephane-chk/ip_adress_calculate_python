from Fonction import Fonction
class AddressTemplate:
    def __init__(self,value_1=0,value_2=0,value_3=0,value_4=0):
        self.setValue1(value_1)
        self.setValue2(value_2)
        self.setValue3(value_3)
        self.setValue4(value_4)
        self.compteurSet = 0
        self.compteurGet = 0
        pass

    def parseInt(self,value):
        try:
            result = int(value)
            return result
        except ValueError:
            raise Exception('Veillez entrer seulement des chiffres')

    def checkValue(self,value):
        if value<0 or value>255:
            raise Exception("Addresse invalide")
        pass

    def getCompteurSet(self):
        return self.compteurSet

    def getCompteurGet(self):
        return self.compteurGet


    def appendValue(self,x):
        x = self.parseInt(x)
        self.checkValue(x)
        if self.getCompteurSet() == 0:
            self.value_1 = x
        elif self.getCompteurSet() == 1:
            self.value_2 = x
        elif self.getCompteurSet() == 2:
            self.value_3 = x
        elif self.getCompteurSet() == 3:
            self.value_4 = x
            pass
        self.compteurSet = self.getCompteurSet() + 1

    def getNextValue(self):
        if self.getCompteurGet() == 0:
            self.compteurGet = self.getCompteurGet() + 1
            return self.getValue1()
        elif self.getCompteurGet() == 1:
            self.compteurGet = self.getCompteurGet() + 1
            return self.getValue2()
        elif self.getCompteurGet() == 2:
            self.compteurGet = self.getCompteurGet() + 1
            return self.getValue3()
        elif self.getCompteurGet() == 3:
            self.compteurGet = self.getCompteurGet() + 1
            return self.getValue4()
            pass

    def setValue1(self, x):
        x = self.parseInt(x)
        self.checkValue(x)
        self.value_1 = x

    def setValue2(self, x):
        x = self.parseInt(x)
        self.checkValue(x)
        self.value_2 = x

    def setValue3(self, x):
        x = self.parseInt(x)
        self.checkValue(x)
        self.value_3 = x

    def setValue4(self, x):
        x = self.parseInt(x)
        self.checkValue(x)
        self.value_4 = x

    def getValue1(self)->int:
        return self.value_1

    def getValue2(self)->int:
        return self.value_2

    def getValue3(self)->int:
        return self.value_3

    def getValue4(self)->int:
        return self.value_4

    def displayToBinary(self)->str:
        return str(Fonction.decimalToBinary(self.getValue1()))+'.'+str(Fonction.decimalToBinary(self.getValue2()))+'.'+str(Fonction.decimalToBinary(self.getValue3()))+'.'+str(Fonction.decimalToBinary(self.getValue4()))

    def displayToDecimal(self)->str:
        return str(self.getValue1())+'.'+str(self.getValue2())+'.'+str(self.getValue3())+'.'+str(self.getValue4())
