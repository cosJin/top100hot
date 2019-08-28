data = [3,2,1,-4,-5,1]
data_1 = data[0::2]

sign = ['+', '+', '+', '*', '+']
data_len = 6
sign_dic = {'*':1, '+':2}

for i in range(data_len-1):
    for j in range(data_len-i-1):
        if data[i] > data[i+1]:
            if sign[i] == '+' or sign[i] == '*':
                if sign[i+1] == '+':
                    temp = data[i]
                    data[i] = data[i+1]
                    data[i+1] = temp
                    i = i-1

for i in range (len(data)):
    print(data[i])

https://www.jianshu.com/p/9923f82af461
https://zhidao.baidu.com/question/238025011.html