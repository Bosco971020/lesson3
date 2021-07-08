import random
ag=1
cro=0
plr=0
ask=1
gsn=0
while ag==1:
    if ask==1:
        ans=random.randint(1,20)
        a=0
        plr=plr+1
    ask=0
    uans=int(input('猜一個1~20的數字')) 
    if a==5:
        print('你太遲了')
        print('上次的答案就算正確也是失敗')
        print('正確答案是',ans)
        print('遊戲結束')
        print('你總共玩了',plr,'次')
        if cro!=0:
             print('你平均每猜',gsn/cro,'次就會猜中答案')
        ag=0
    elif uans>ans:
        a=a+1
        print('你猜的數字太大了')
        gsn=gsn+1
        print('再猜一次吧')
        ag=1
    elif uans<ans:
        a=a+1
        print('你猜的數字太小了')
        gsn=gsn+1
        print('再猜一次吧')
        ag=1
    elif uans==ans:
        print('你猜對了')
        cro=cro+1
        gsn=gsn+1
        ask=int(input('你想再玩一次嗎?是的話輸入1，不是的輸入2'))
        if ask==1:
            ag=1
        elif ask==2:
            ask=0
            print('那麼遊戲就結束囉')
            print('你總共玩了',plr,'次')
            print('你平均每猜',gsn/cro,'次就會猜中答案')
       
        