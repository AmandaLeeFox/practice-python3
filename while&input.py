#while循环0-5
current = 0 
while current <= 5:
    print(current) 
    current +=1 #打印后加循环


#定义了一个退出值，只要用户输入的不是这个值，程序就接着运行
message = ''
show1 = 'u can leave a message,and input quit to end.'
while message != 'quit':
    message = input(show1)
    print(message)

	
#定义了一个退出值，只要用户输入的不是这个值，程序就接着运行
message = ''
show1 = 'u can leave a message,and input quit to end.'
while message != 'quit':
    message = input(show1)
    if message != 'quit': #为了不打印quit
        print(message)


#可定义变量为“标志”，若True时则运行
message = ''
show1 = 'u can leave a message,and input quit to end.'
active = True
while active:
    message = input(show1)
    if message == 'quit':
        active = False
    else:
        print(message)

		
#[break]让用户指出他到过哪些地方, 输入'quit' 后使用break, 退出while循环
message = ''
show1 = 'pls enter a city you have been there.'
show1 += 'enter quit to end'
while True:
    message = input(show1)
    if message == 'quit':
        break
    else:
        print(message)

#continue，返回到循环开头，判定是否继续，1-10打印偶数循环
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


'''
比萨配料
编写一个循环，提示用户输入一系列的比萨配料, 并在用户输入'quit' 时结束循环
每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
'''

choices = ''
show1 = 'enter your pizza choices:'
while True:
    choices = input(show1)
    if choices == 'quit':
        break
    else:
        print('we are going to add ' + choices + ' in your pizza')

'''
电影票
根据观众年龄收取不同的票价
不到3岁的观众免费;3~12岁的观众为10美元;超过12岁的观众为15美元
请编写一个循环，在其中询问用户的年龄，并指出其票价。
'''

age = int(input('enter your age pls:'))
if age <= 3:
    price = 0
elif age >= 12:
    price = 15
else:
    price = 10
print('your price is: ' + str(price))


