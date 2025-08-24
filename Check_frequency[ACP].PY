dict={'Codingal':3,'is':2,'best':2,'for':2,'Coding':1}
print("The original dictionary:"+str(dict))
k=int(input("Enter a value for which you want to check the frequency:"))
count=0
for key in dict:
    if dict[key]==k:
        count=count+1
print("Frequency of",k,"is:"+str(count))