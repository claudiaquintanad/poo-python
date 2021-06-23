import statistics

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result = self.result + num
        for num in nums:
            self.result = self.result + num
        return self
    def subtract(self, num, *nums):
        self.result = self.result - num
        for num in nums:
            self.result = self.result - num
        return self
# crear una instruccion:
md = MathDojo()

# para probar:
#x = md.add(5,2,6,3).add(1).add(1,1,1).result
#x = md.subtract(3).subtract(5,3,8).subtract(2).result


x = md.add(2).add(2,5,1).subtract(3,2).result
print(x) # debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!


#desviación estandar
dev = statistics.pstdev([4,5,76,2,4,7,2])
print(dev)
