#函数返回值
#可使用return语句将值返回到调用函数的代码行

#返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
me = get_formatted_name('Amanda','Lee')
print(me)

#可选的实参
