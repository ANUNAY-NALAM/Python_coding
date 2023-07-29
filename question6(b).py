class Account:
    def __init__(self,card_no,pin,balance,withdraw_amount,account_type):
        self.card_no=card_no
        self.pin=pin
        self.balance=balance
        self.withdraw_amount=withdraw_amount
        self.account_type=account_type
    def method1(self,withdraw_val):
        if withdraw_val<=self.withdraw_amount:
            self.balance=self.balance-withdraw_val
        self.withdraw_amount=withdraw_val
    
class ATM(Account):
    def __init__(self,account_list):
        self.account_list=account_list
    def method2(self,m_card,m_pin,m_wa):
        for obj in account_list:
            if obj.card_no==m_card and obj.pin==m_pin:
                obj.method1(m_wa)
                return obj
        return None
    def method3(self,m_acty):
        ans_dic={}
        for obj in account_list:
            if m_acty.upper()==obj.account_type.upper():
                ans_dic[obj.card_no]=obj.balance
        return ans_dic
account_list=[]
for _ in range(int(input())):
    card_no=int(input())
    pin=int(input())
    balance=float(input())
    withdraw_amount=float(input())
    account_type=input()
    account_list.append(Account(card_no,pin,balance,withdraw_amount,account_type))
obj=ATM(account_list)
m_card=int(input())
m_pin=int(input())
m_wa=int(input())
res=obj.method2(m_card,m_pin,m_wa)
print(res.card_no,res.balance,res.withdraw_amount)
m_acty=input()
dic=obj.method3(m_acty)
dic1 =dict(sorted(dic.items(),key= lambda items:items[1]))
for k,v in dic1.items():
    print(k,v)