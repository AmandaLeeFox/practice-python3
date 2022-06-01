#函数返回值
#可使用return语句将值返回到调用函数的代码行

#返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
me = get_formatted_name('Amanda','Lee')
print(me)


# 实参变为可选的，给某个值设定一个空字符，未提供时不使用
def get_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' +last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
me = get_name('Amanda', 'Lee')
me2 = get_name('Amanda', 'Lee', 'mid') #按照实参顺序
print(me)
print(me2)


#返回字典，【定义函数，返回字典，包含一个人的信息，并加年龄信息未默认空值参数】
def get_person(first_name, last_name, age = ''):
    person = {
        'first_name' : first_name,
        'last_name' : last_name
    }
    if age:
        person['age'] = age #如果有age，则加入字典
    return person
me = get_person('Amanda', 'Lee', 27) #或age = 27
print(me)
