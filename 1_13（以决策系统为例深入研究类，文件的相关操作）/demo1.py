class Judge:
    flag=0
    def __init__(self,judge1,judge2,judge3):
        self.judge1=judge1
        self.judge2=judge2
        self.judge3=judge3
    def decide(self,judge1,judge2,judge3):
        if self.judge1=='pass' and self.judge2=='pass':
            self.flag=1
        else:
            if self.judge1=='pass' or self.judge2=='pass':
                if ((self.judge1=='pass') and (self.judge3=='pass')) or ((self.judge2=='pass') and (self.judge3=='pass')):
                    self.flag=1
                else:
                    self.flag=0
            else:
                self.flag=0
class Aspect1(Judge):
    def __init__(self,judge1,judge2,judge3,aspect1):
        #super()为返回父类去寻找对应函数
        super().__init__(judge1,judge2,judge3)
        self.aspect1=aspect1
    def decide(self,judge1,judge2,judge3,aspects1):
        super().decide(judge1,judge2,judge3)
        if self.flag and self.aspect1>=60:
            print('pass')
        else:
            print('not pass')
a=input('first judge:')
b=input('second judge:')
c=input('third judge:')
d=int(input('the score:'))
t=Aspect1(a,b,c,d)
t.decide(a,b,c,d)
