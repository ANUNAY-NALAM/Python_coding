st=[]
n=int(input())
for _ in range(n):
    st.append(input())
for i in range(n):
    count=0
    for j in st[i]:
        if j != 'a' and j!= 'e'and j!='i' and j!='o' and j!='u':
            continue
        else:
            count+=1
    if count <=1:
        print(st[i],"(",count,')')