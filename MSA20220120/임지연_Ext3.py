홍길동1 = [95, 90, 80, 50]
홍길동2 = [100, 50, 90, 90]
홍길동3 = [99, 60, 100, 40]
홍길동4 = [55, 80, 80, 60]


def sumOne(input):
    sum = 0
    i = 0
    while True:
        if i < len(input):
            sum += input[i]
            i = i+1
        else: return sum 


def meanOne(input):
    return (input/4)
    
def sumAll():
    return (sum1 + sum2 + sum3 + sum4)

def meanAll():
    return (sum1 + sum2 + sum3 + sum4)/16
        


sum1 = sumOne(홍길동1) # 315
meanOne(sum1) # 78.75
sum2 = sumOne(홍길동2) # 330
meanOne(sum2) # 82.5
sum3 = sumOne(홍길동3) # 299 
meanOne(sum3) # 74.75
sum4 = sumOne(홍길동4) # 275
meanOne(sum4) # 68.75


sumAll() #1219
meanAll() #76.1875



temp = 0