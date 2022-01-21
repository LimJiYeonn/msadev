홍길동1 = [95, 90, 80, 50]
홍길동2 = [100, 50, 90, 90]
홍길동3 = [99, 60, 100, 40]
홍길동4 = [55, 80, 80, 60]


def sumOne(input):
    sum = 0
    i = 0
    while len(input) > 0:
        sum += input.pop(i)
    return sum


sum1 = sumOne(홍길동1) # 315
mean1 = sum1/4

sum2 = sumOne(홍길동2) 
mean2 = sum2/4

sum3 = sumOne(홍길동3) 
mean3 = sum3/4

sum4 = sumOne(홍길동4)
mean4 = sum4/4


sumAll = sum1 + sum2 + sum3 + sum4 #1219
meanAll = (mean1 + mean2 + mean3 + mean4) / 4 



temp = 0