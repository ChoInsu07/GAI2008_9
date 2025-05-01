class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __neg__(self):
        return Complex(-self.a,-self.b)

    def __add__(self, operand):
        new_a = self.a + operand.a
        new_b = self.b + operand.b
        return Complex(new_a,new_b)
    
    def __sub__(self, operand):
        new_a = self.a - operand.a
        new_b = self.b - operand.b
        return Complex(new_a,new_b)
    
    def __mul__(self, operand):
        new_a = self.a * operand.a
        new_b = self.b * operand.b
        return Complex(new_a,new_b)
    
    def __str__(self):
        if self.b < 0 :
            return f"{self.a} + ({self.b})i"
        else :
            return f"{self.a} + {self.b}i"

if __name__ == '__main__':
    A = Complex(1,2)
    B = Complex(4,2)
    print(-A)
    print(A+B)
    print(A-B)
    print(A*B)
