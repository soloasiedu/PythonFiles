class Pow:
    def pow(x, n):
        total = x
        if n == 0:
            return 1
        elif n > 0:
            for i in range(1, n):
                total = total * x
            return total
        else:
            return 1/pow(x, abs(n))



print(Pow.pow(2,-3))
    
