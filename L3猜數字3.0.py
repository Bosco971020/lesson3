ag=1
end=0
cro=0
plr=0
ask=0
a=0

while ag==1:
    ask=0
    import random
    ans=random.randint(1,20)
    plr=plr+1
    gsn=0
    a=0
    uans=int(input('猜一個1~20的數字'))
    g=1
    a=a+1
    ag=0
while g==1:
    if a>5:
        print('你已經沒機會了')
        print('正確答案是',ans)
        print('遊戲結束')
        print('你總共玩了',plr,'次')
        if cro!=0:
             print('你平均每猜',gsn/cro,'次就會猜中答案')
        end=0
        g=0
    elif uans>ans:
        print('你猜的數字太大了')
        gsn=gsn+1
        a=a+1
        uans=int(input('再猜一次吧'))
        g=1
    elif uans<ans:
        print('你猜的數字太小了')
        gsn=gsn+1
        a=a+1
        uans=int(input('再猜一次吧'))
        g=1
    elif uans==ans:
        print('你猜對了')
        cro=cro+1
        g=0
        gsn=gsn+1
        ask=int(input('你想再玩一次嗎'))
        if ask==1:
            ag=1
        elif ask==2:
            ask=0
            print('那麼遊戲就結束囉')
            print('你總共玩了',plr,'次')
            if cro!=0:
                print('你平均每猜',gsn/cro,'次就會猜中答案')
       
        