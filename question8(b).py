class Employee:
    def __init__ (self,emp_id,emp_name,role,age):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.role=role
        self.age=age
        self.pro_elg=None
class Organization:
    def __init__(self,emp_list,age_dict):
        self.emp_list=emp_list
        self.age_dict=age_dict
    def eligibility_status(self) :
        details = {}
        for obj in self.emp_list:
            for k,v in self.age_dict.items():
                if obj.role.lower()==k.lower():
                    if obj.age==v:
                        details[obj.emp_id]="eligible"
                        obj.pro_elg=True
                    elif obj.age>v:
                        details[obj.emp_id]="overdue"
                        obj.pro_elg=True
                    else:
                        details[obj.emp_id]=str(v-obj.age)+"years left"
        return details
        
emp_list=[]
n=int(input())
for _ in range(n):
    emp_id=int(input())
    emp_name=input()
    role=input()
    age=int(input())
    emp_list.append(Employee(emp_id,emp_name,role,age))
age_dict={}
for _ in range(3):
    key=input()
    val=int(input())
    age_dict[key]=val
obj=Organization(emp_list,age_dict)
res_dict=obj.eligibility_status()
for k,v in res_dict.items():
    print(k,":",v)