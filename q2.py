string=str(input("enter the string where the character to be counted: "))
dictkey=dict()
for i in string:
    if i in dictkey:
        dictkey[i]+=1
    else:
        dictkey[i]=1

print("the count of character is: ",dictkey)