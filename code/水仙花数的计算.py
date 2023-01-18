def judge(a):
    sum=0
    while a:
       sum+=1
       a//=10
    return sum
max=int(input('请输入最大数：'))
if max>100:
    num=0
    print('100 到 %d 的水仙花数有：' % max,end='\t')
    for i in range(100,max):
        n=judge(i)
        sum=0
        a=0
        for j in range(n):
            k=i
            while k:
                a=k%10
                sum+=int(a**n)
                k//=10
            if sum==i:
                print(i,end='\t')
                num+=1
    print()
    print('水仙花数的个数为：', num)

else:
    print('最大数应大于100！')

