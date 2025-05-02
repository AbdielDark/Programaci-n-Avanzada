class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar(self):
        return self.num1 + self.num2 + self.num3

    def mayor(self):
        return max(self.num1, self.num2, self.num3)

    def menor(self):
        return min(self.num1, self.num2, self.num3)

    def iguales(self):
        return self.num1 == self.num2 == self.num3

    def concatenar(self):
        return f"{self.num1}{self.num2}{self.num3}"
    
obj = Mi_Clase(3, 3, 3)
print("Suma:", obj.sumar())              # 9
print("Mayor:", obj.mayor())            # 3
print("Menor:", obj.menor())            # 3
print("¿Iguales?:", obj.iguales())      # True
print("Concatenar:", obj.concatenar())  # "333"