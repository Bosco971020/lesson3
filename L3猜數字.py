import random
num=random.randint(1,10)
ans=int(input('請猜一個1~10的數字'))
if num==ans:
    print('你猜對了')
    print('答案就是',num)
else:
    print('你猜錯了')
    print('正確答案是',num)