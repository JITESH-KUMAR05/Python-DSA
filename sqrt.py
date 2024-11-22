def mySqrt(x: int) -> int:
    a = x
    b = 1
    while a>b:
        a = (a+b)//2
        b = x//a
    return a
    

print(mySqrt(4)) # 2