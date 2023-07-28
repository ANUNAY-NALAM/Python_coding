def get_pos(n,st,req):
    p=-1
    for ob in range(len(st)):
        if st[ob]==req:
            p=ob
    return p


n=int(input())
st=[]
for _ in range(n):
   st.append(input())

req=input()
print(get_pos(n,st,req))