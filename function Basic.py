#定义函数
def greet_user():
    print('hello')
greet_user() #调用函数


#传递实参
def greet_user(name): #传递name参数，形参
    print('hello, ' + name.title() + '!')
greet_user('liya') #传递name参数的值，实参，记得加引号，因为不是变量，只是个参数


#传递实参：位置实参+关键字实参
def describe_pet(pet_type, pet_name):
    print('I have a ' + pet_type)
    print("My " + pet_type + "'s name is " + pet_name)
describe_pet('cat', 'Mihua') #位置实参，以顺序为主
describe_pet(pet_type = 'dog', pet_name = 'Benben') #关键字实参，直接定义


#传递实参：行参可设置默认值
def describe_pet(pet_name, pet_type = 'dog'): #默认值要放在最后
    print('I have a ' + pet_type)
    print("My " + pet_type + "'s name is " + pet_name)
describe_pet(pet_name = 'Benben') #也可以直接写实参，不定义

# ——————————————————————————例子练习开始——————————————————————————

'''
编写一个名为make_shirt() 的函数, 它接受一个尺码以及要印到T恤上的字样
这个函数应打印一个句子，概要地说明T恤的尺码和字样。
使用位置实参调用这个函数来制作一件T恤, 再使用关键字实参来调用这个函数。
'''

def make_shirt(size, text):
    print("your shirt's size is " + size + ", and text is " + text)
make_shirt('M','Amanda')

'''
使其在默认情况下制作一件印有字样“I love Python”的大号T恤
调用这个函数来制作如下T恤:
一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤(尺码无关紧要)
'''

def make_shirt(size, text = 'I love Python'):
    print("your shirt's size is " + size + ", and text is " + text)
make_shirt('L')
make_shirt('M')
make_shirt('M',text = 'change')

# ——————————————————————————例子练习结束——————————————————————————



