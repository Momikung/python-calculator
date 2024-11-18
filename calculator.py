class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return  a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
     if b == 0:
        return "divisor can't be 0"

    # ตรวจสอบสัญลักษณ์ของผลลัพธ์
     negative_result = False
     if a < 0 and b > 0 or a > 0 and b < 0:
        negative_result = True

    # ทำให้ a และ b เป็นบวก
     if a < 0:
        a = -a
     if b < 0:
        b = -b

    # คำนวณผลหารแบบลบซ้ำ
     result = 0
     while a >= b:
        temp = b
        while a >= temp:
            a -= temp
            result += 1

    # ปรับสัญลักษณ์ของผลลัพธ์
     if negative_result:
        result = -result

     return result

    
    def modulo(self, a, b):
     if b == 0:
        return "divisor can't be 0"

    # ทำให้ b เป็นบวกเสมอ
     if b < 0:
        b = -b

    # คำนวณโมดูลัสแบบทีละขั้น
     if a < 0:
        while a < 0:
            a += b
     else:
        while a >= b:
            a -= b

     return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(5, 2))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: division: ", calc.divide(5, 2))
    print("Example: modulo: ", calc.modulo(5, 2))
   
