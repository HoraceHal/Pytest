# i = 0
# while i < 10:
#     print('是')
#     i+=1


# i = 0
# while i < 10:
#     print('循环了第%d次'% (i+1)) 
#     print('i=%d'% i)
#     i+=1


# 计算1-100的累加和

# index = 0
#
# my_sum = 0
#
# while index <= 100:
#     print(index)
#     my_sum += index
#     index+=1
# print(my_sum)


i = 1
c = 1
while i < 101:
    print(c)
    if i % 2 != 0:
        c = c + i
    i += 1
