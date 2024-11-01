import random as rd

count = 0
for i in range(5):
    a = rd.randint(1,20)
    b = rd.randint(1,20)

    print(f'how much is {a}+{b}')
    result = int(input())
    if result == a+b:
        print('you are correct!!')
        count +=1
    else:
        print('I am stupid')
        count +=1
print(f'you are corrent {count} time')
# print(a)
# print(b)
# print(a+b)
# print(result)