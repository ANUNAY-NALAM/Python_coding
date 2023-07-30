class Account:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
    def method1(self,dep_amt):
        self.balance=self.balance+dep_amt
        return self.balance
    def method2(self,with_amt):
        p=self.balance-with_amt
        if p<1000:
            return 0
        else:
            self.balance=self.balance-with_amt
            return p
acc_no=int(input())
name=input()
balance=int(input())
obj=Account(acc_no,name,balance)
p=input()
if p=='d':
    print(obj.method1(int(input())))
if p=='w':
    k=obj.method2(int(input()))
    if k==0:
        print("insuffcient amount")
    else:
        print(k)