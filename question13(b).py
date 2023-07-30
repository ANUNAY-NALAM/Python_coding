class Employee:
    def __init__(self,emp_no,emp_name,leaves):
        self.emp_no=emp_no
        self.emp_name=emp_name
        self.leaves=leaves
class Company:
    def __init__(self,emps):
        self.emps=emps
    def leave_avalilable(self,emp_num,leave_type,num_leave):
        for obj in self.emps:
            if obj.emp_no==emp_num:
                for k,v in obj.leaves.items():
                    if k==leave_type:
                        if v>=num_leave:
                            print('Granted')
                        else :
                            print('Rejected')
emps=[]
for _ in range(int(input())):
    emp_no=int(input())
    emp_name=input()
    leaves={}
    leaves['EL']=int(input())
    leaves['CL']=int(input())
    leaves['SL']=int(input())
    emps.append(Employee(emp_no,emp_name,leaves))
obj=Company(emps)
emp_num=int(input())
leave_type=input()
num_leave=int(input())
res=obj.leave_avalilable(emp_num,leave_type,num_leave)