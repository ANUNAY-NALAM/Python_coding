st11=input()
st22=input()


for i in range(len(st1)):
    flag=0
    for j in range(len(st2)):
        if st1[i]==st2[j]:
            flag=1
        
    if flag==0:
        break;
if flag:
    print("string is valid")
else:
    print("string is invalid")