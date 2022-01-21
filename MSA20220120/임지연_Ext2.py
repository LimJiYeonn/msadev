홍길동1 = [95, 90, 80, 50]
홍길동2 = [100, 50, 90, 90]
홍길동3 = [99, 60, 100, 40]
홍길동4 = [55, 80, 80, 60]


def sumOne(input):
    sum = 0
    i = 0
    while i < len(input):
        sum += input[i]
        i = i+1
    return sum


def meanOne(input):
    size = len(input)
    return sumOne(input)/size
    
def sumAll():
    return (sumOne(홍길동1) + sumOne(홍길동2) + sumOne(홍길동3) + sumOne(홍길동4))

def meanAll():
    return sumAll()/16
        


sumOne(홍길동1) # 315
meanOne(홍길동1) # 78.75
sumOne(홍길동2) # 330
meanOne(홍길동2) # 82.5
sumOne(홍길동3) # 299 
meanOne(홍길동3) # 74.75
sumOne(홍길동4) # 275
meanOne(홍길동4) # 68.75


sumAll() #1219
meanAll() #76.1875



temp = 0