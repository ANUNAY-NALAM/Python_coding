st=[]
for _ in range(int(input())):
    st.append(input())
for pt in st:
    n=len(pt)
    flag=0
    for i in range(n):
        if pt[i] is not pt[n-i-1]:
            flag=1
    if flag==0:
        print(pt)