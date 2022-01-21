홍길동1 = [95, 90, 80, 50]
홍길동2 = [100, 50, 90, 90]
홍길동3 = [99, 60, 100, 40]
홍길동4 = [55, 80, 80, 60]


def sum(input):
    sum = 0
    for i in input:
        sum += i
    return sum


def mean(input):
    sum = 0
    for i in input:
        sum += i
    return (sum / len(input))
    

sum(홍길동1) # 315
mean(홍길동1) # 78.75
sum(홍길동2) # 330
mean(홍길동2) # 82.5
sum(홍길동3) # 299 
mean(홍길동3) # 74.75
sum(홍길동4) # 275
mean(홍길동4) # 68.75

all = 홍길동1 + 홍길동2 + 홍길동3 + 홍길동4

sum(all) #1219
mean(all) #76.1875



temp = 0