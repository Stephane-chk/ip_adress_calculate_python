class Fonction:
    @staticmethod
    def decimalToBinary(n):
        result = bin(n).replace("0b", "")
        if len(result)<8:
            compteur = len(result)
            while(compteur<8):
                result = '0'+result
                compteur += 1
        pass
        return result

    @staticmethod
    def binaryToDecimal(binary):
        i, integer = 0, 0
        size = len(binary)
        while i < len(binary):
            integer += int(binary[size - 1 - i]) * pow(2, i)
            i += 1
        return integer

    @staticmethod
    def logicalAND(a:int,b:int):
        result = bin(a & b).replace("0b", "")
        return result

    @staticmethod
    def logicalOR(a:int,b:int):
        result = bin(a | b).replace("0b", "")
        return result

    @staticmethod
    def generateDecimal(nbBits:int):
        result = "";
        compteur = 0
        while(compteur<nbBits):
            result = '1'+result
            compteur += 1
            pass
        if len(result)<8:
            compteur = len(result)
            while(compteur<8):
                result = result+'0'
                compteur += 1
                pass
            pass
        return Fonction.binaryToDecimal(result)

