# if——else

# 定义一个变量
# a = not True
# if a:
#     print(1)
# else:
#     print(2)
#
#
# had = int(input('输入身高：'))
# if had <= 150:
#     print('不能进去')
# else:
#     print('可以进去')


score = 89

if 90 >= score <= 100:
    print('优秀')
elif 80 >= score < 90:
    print('良好')
elif 70 >= score < 80:
    print('一般')
elif 60 >= score < 70:
    print('及格')
else:
    print('不及格')