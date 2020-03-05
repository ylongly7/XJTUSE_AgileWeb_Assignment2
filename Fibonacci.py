class Fibonacci:
    @classmethod
    def of(cls,n):
        a,b = 1,1
        i = 2
        while i<=n:
            a,b = b,a+b
            i+=1
        return a
if __name__ == '__main__':
    for i in range(1,201):
        print(Fibonacci.of(i))