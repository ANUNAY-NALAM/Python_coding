class painting:
    def __init__(self,p_id,p_name,p_price,p_type):
        self.p_id=p_id
        self.p_name=p_name
        self.p_price=p_price
        self.p_type=p_type
class showRoom:
    def __init__(self,p_list):
        self.p_list=p_list
    def method1(self,paint_type):
        sum=0
        isFound=False
        for obj in self.p_list:
            if obj.p_type.lower()==paint_type.lower():
                sum=sum+obj.p_price
                isFound=True
        if isFound:
            return sum
        else :
            return "no painting Found"
    def method2(self):
        dic={}
        for obj in self.p_list:
            if obj.p_name not in dic:
                dic[obj.p_name]=1
            else:
                dic[obj.p_name]+=1
        dic1 = dict(sorted(dic.items(), key = lambda item:item[1], reverse=True))
        lis=[]
        for k,v in dic1.items():
            if len(lis)==0:
                lis.append(k)
                temp=v
            else:
                if temp==v:
                    lis.append(k)
                else:
                    break
        lis.sort()
        return lis[0]
p_obj=[]
for _ in range(int(input())):
    p_id=int(input())
    p_name=input()
    p_price=int(input())
    p_type=input()
    p_obj.append(painting(p_id,p_name,p_price,p_type))
obj=showRoom(p_obj)
paint_type=input()
t_price=obj.method1(paint_type)
painter=obj.method2()
print(t_price)
print(painter)