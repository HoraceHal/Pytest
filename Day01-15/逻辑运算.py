# and
name = 'lilin'
pasw = '1234567'

# and 同真为真，一假为假
if name == 'lilin' and pasw == '123456':
    print('登录成功')

# or 同假则假，一真则真
if name != 'lilin' or pasw != '123456':
    print('登录失败')

# not 非真则假，非假则真  取反
is_man = False
if not is_man:
    print('男的')