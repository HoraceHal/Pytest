# 猜拳程序

person = int(input('输入：剪刀(0) 石头(1) 布(2):') )

# 计算机输入的数
import random

compute = random.randint(0,2) 
print(compute)


if (person ==0 and compute == 2) or (person==1 and compute==0) or (person==2 and compute==1):
    print('你赢了')
elif person == compute:
    print('平局')
else:
    print('你输了')    