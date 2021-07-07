import random
num=random.randint(1,10)
uans=int(input('請猜一個1~10的數字，要猜到對才能停'))



while num!=uans:
    print('你猜錯了')
    print('你的答案是',uans)
    uans=int(input('再猜一次'))
if  num==uans:
    print('你猜對了')
    print('正確答案是',num)   

    
   
    