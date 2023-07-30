class Employee:
    def __init__(self,name,designation,salary,Loan_dict):
       self.name=name
       self.designation=designation
       self.salary=salary
       self.Loan_dict=Loan_dict
class Oraganization:
    def __init__(self,emp_list,loan_list,max_dict):
        self.emp_list=emp_list
        self.loan_list=loan_list
        self.max_dict=max_dict
    def method1(self,e_name,e_loanType,e_amount):
        for obj in self.emp_list:
            if obj.name.lower()==e_name.lower() and e_loanType.lower() not in obj.Loan_dict and e_loanType.lower() in self.loan_list:
                sum=e_amount
                for _,v in obj.Loan_dict.items():
                    sum=sum+v
                for key,val in self.max_dict.items():
                    if key==obj.designation.lower():
                        if sum<val:
                            obj.Loan_dict[e_loanType]=e_amount
                            return obj
                        else:
                            return False
        return False


emp_list=[]
for _ in range(int(input())):
    name=input()
    designation=input()
    salary=int(input())
    Loan_dict={}
    for _ in range(int(input())):
        key=input()
        val=int(input())
        Loan_dict[key]=val
    emp_list.append(Employee(name,designation,salary,Loan_dict))

loan_list=[]
for _ in range(int(input())):
    loan_list.append(input().lower())
max_dict={}
for _ in range(int(input())):
    key=input().lower()
    val=int(input())
    max_dict[key]=val
e_name=input()
e_loanType=input()
e_amount=int(input())
obj=Oraganization(emp_list,loan_list,max_dict)
res=obj.method1(e_name,e_loanType,e_amount)
if res:
    print("loan granted")
    for k,v in res.Loan_dict.items():
        print(k,":",v)
else:
    print("falied")