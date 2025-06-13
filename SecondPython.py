# Second cahpter in Python
name = str(input("what is your name : "))

print(name, len(name))
print(name.count("a"))

# Conditional Statement
exp = int(input("how much exp. in Networking: "))

if(exp>=15 and exp<=20):
    Designation = "You are eligible for Operation Manger"
elif(exp>=10 and exp<15):
    Designation = "You are eligible for Team Lead"
elif(exp>=5 and exp<10):
    Designation = "You are eligible for Network Engineer"
elif(exp>1 and exp<5):
    Designation = "You are eligible for Associate Engineer"
else:
    Designation = "Sorry, you are not eligible"

print(Designation)

num = 1

while num <=99:
    num += 1
    print (num)

print (num)
