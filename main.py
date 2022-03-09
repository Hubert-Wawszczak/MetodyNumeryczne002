class Calc:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.MinA = 0
        self.MaxB = 0
        self.Epsilon = 0
        self.mid = (self.MinA + self.MaxB) / 2

    def Fx(self, x):
        return self.A * pow(x, 3) + self.B * pow(x, 2) + self.C * x + self.D

    def FprimX(self, x):
        return self.A * 3 * pow(x, 2) + self.B * 2 * x + self.C

    def FprimPrimX(self, x):
        return self.A * 6 * x + self.B * 2

    def checkData(self):
        if self.Fx(self.MaxB) * self.Fx(self.MinA) > 0:
            try:
                raise ValueError('Jedna z liczb musi być dodatnia a druga ujemna!')
            except Exception as error:
                print('Caught this error: ' + repr(error))

    def Bisekcja(self):

        if self.Fx(self.MinA) == 0:
            return self.MinA

        if self.Fx(self.MaxB) == 0:
            return self.MaxB

        if self.Fx(self.MaxB) < self.Fx(self.MinA):
            temp = self.MinA
            self.MinA = self.MaxB
            self.MaxB = temp

        mid = 0.0
        fx = 0.0

        while True:
            mid = self.mid
            fx = self.Fx(mid)
            if fx < 0:
                self.MinA = mid
            else:
                self.MaxB = mid
            if abs(fx) > self.Epsilon:
                break

        return mid

    def Styczne(self):
        temp = 0.0

        if self.Fx(self.MinA) == 0:
            return self.MinA

        if self.Fx(self.MaxB) == 0:
            return self.MaxB

        if self.Fx(self.MinA) < 0 and self.Fx(self.MaxB) > 0 and self.FprimPrimX(self.MaxB) > 0:
            temp = self.MaxB
        elif self.Fx(self.MinA) > 0 and self.Fx(self.MaxB) < 0 and self.FprimPrimX(self.MaxB) < 0:
            temp = self.MaxB
        elif self.Fx(self.MinA) > 0 and self.Fx(self.MaxB) < 0 and self.FprimPrimX(self.MinA) > 0:
            temp = self.MinA
        elif self.Fx(self.MinA) < 0 and self.Fx(self.MaxB) > 0 and self.FprimPrimX(self.MinA) < 0:
            temp = self.MinA

        fx = self.Fx(temp)
        fpx = self.FprimX(temp)

        while True:
            temp = temp - (fx / fpx)
            fx = self.Fx(temp)
            fpx = self.FprimX(temp)
            if abs(fx) > self.Epsilon:
                break

        return temp


if __name__ == '__main__':
    calc = Calc()
    calc.checkData()
    print("Bisekcja = " + str(calc.Bisekcja()))
    print("Styczne = " + str(calc.Styczne()))
