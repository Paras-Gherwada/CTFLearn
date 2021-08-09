f=open("data.dat","r")
lines=f.readlines()

count=0

for i in lines:
    if i.count("0")%3==0 or i.count("1")%2==0:
        count=count+1

print count
