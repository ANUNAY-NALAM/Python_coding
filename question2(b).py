class Employee:
    def __init__(self,emp_name,designation,salary,overTimeContribution):
        self.emp_name=emp_name
        self.designation=designation
        self.salary=salary
        self.overTimeContribution=overTimeContribution
        self.overTimeStatus=False
class Organization:
    def __init__(self,emp_list):
        self.emp_list=emp_list
    def isEligible(self,overTimeThreshold):
        for obj in self.emp_list:
            sum=0
            for k,v in obj.overTimeContribution.items():
                sum=sum+v
            if sum>=overTimeThreshold:
                obj.overTimeStatus=True
    def total_bonus(self,rate_per_hour):
        total_b=0
        for obj in self.emp_list:
            sum=0
            for k,v in obj.overTimeContribution.items():
                sum=sum+v 
            if obj.overTimeStatus:
                total_b +=sum*rate_per_hour
        return total_b;


n =int(input())
emp_list=[]
for _ in range(n):
    emp_name=input()
    designation=input()
    salary=int(input())
    overTimeContribution={}
    for _ in range(int(input())):
        key=input()
        val=int(input())
        overTimeContribution[key]=val
    emp_list.append(Employee(emp_name,designation,salary,overTimeContribution))

obj=Organization(emp_list)
overTimeThreshold=int(input())
rate_per_hour=int(input())
obj.isEligible(overTimeThreshold)
total_b=obj.total_bonus(rate_per_hour)

for i in emp_list:
    print(i.emp_name,":",i.overTimeStatus)
print(total_b)
        
