class Employee:
    def __init__(self,emp_Id,emp_name,emp_role,emp_sal):
        self.emp_Id=emp_Id
        self.emp_name=emp_name
        self.emp_role=emp_role
        self.emp_sal=emp_sal
    def method1(self,per_num):
        self.emp_sal=(self.emp_sal*(100+per_num))/100
        return self.emp_sal


class Organization:
    def __init__(self,emp_list):
        self.emp_list=emp_list
    def method2(self,med_role,med_per):
        sal_inc_emp=[]
        for obj in self.emp_list:
            if obj.emp_role==med_role:
                res=obj.method1(med_per)
                sal_inc_emp.append([obj.emp_name,res])
        return sal_inc_emp


emp_list=[]
for _ in range(int(input())):
    emp_Id=int(input())
    emp_name=input()
    emp_role=input()
    emp_sal=int(input())
    emp_list.append(Employee(emp_Id,emp_name,emp_role,emp_sal))
obj=Organization(emp_list)
med_role=input()
med_per=int(input())
res=obj.method2(med_role,med_per)
for i in res:
    print(i[0])
    print(i[1])