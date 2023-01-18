#w为只写，r为只读，a为追加写入，+使模式变为读写；w写入的会覆盖原有的，a则是追加写入
with open('D:/霜降2.png','rb') as image:
    #以二进制下的只读方式打开D盘中一个名为霜降2的png文件，并将其起名为image
    with open('copyimage1','wb') as copyimage:
        #以二进制下的写入方式打开copyimage1，若没有则创建一个该文件，并将其起名为copyimage
        copyimage.write(image.read())
        #将image中读取到的内容写入copyimage，完成文件的复制

#用with不用加上close语句，不用with则需要close语句来关闭文件
fp=open('text.txt','a+')
fp.write('nb')
fp1=open('text.txt','r')
c=fp1.read()
print(c)
fp.close()