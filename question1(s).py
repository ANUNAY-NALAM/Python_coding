'''
Write a python code to print the count of valid strings 
and invalid strings from a given list of strings

A string is considered as valid if it contains combinations
of alphabetes (in upper case or lower case) with/without 
spaces.

Define a function to check if a given string is valid or not
i.e if it contains combination of alphabetes.

This function will take string as input and return True 
if the string is valid, otherwise will return False.
Input:
4
HelloGood Morning
abcd123Fghy
India
Progoto.c

Output:
Count Of Valid String = 2
Count of Invalid String = 2
'''

def get_ans(str_in):
    valid = 0
    in_valid = 0
    for st in str_in:
        
        p = ''
        for pt in st.split():
            p = p + pt.strip()
        if p.isalpha():
            valid += 1
        else:
            in_valid += 1
    return [valid, in_valid]
           

n = int(input( ))
str_in = []
for _ in range(n):
    str_in.append(input())

valid, in_valid = get_ans(str_in)

print("No of valid arrays:", valid)

print("No of invalid arrays:", in_valid)