
#num = 100

#while num >= 1:
 #   print (num)
  #  num -= 1

#print(num)

# n = int(input("your table number: " ))
# i = 1
# while i <=10:
#    print (n*i)
#    i +=1


# mobile = (8443910056, 9674423685, 9239417975, 8240129420, 9239381348 )

# number = int(input("put your number:"))
# id = 0
# while id < len(mobile):
#     if (mobile[id] == number):
#         print("found your number in the list ", id)
#         break

#     else: 
#         print ("number not listed.")
#     id +=1
    
# while id < len(mobile):
#     if (mobile[id] == number):
#         id +=1
#         print("found your number in the list ", id)
#         continue

#     else: 
#         print ("number not listed.")
#     id +=1
    
#For Loop
# nums = [1, 4, 9, 16, 25, 36]

# for value in nums:
#     print(value)

roll =(5, 8, 7, 85, 58, 75, 57,)

XX = int(input("what is your roll N0. :"))

i = 0

for el in roll:
    if (el == XX):
        print("you are pass and rank:", i)
        break
    i += 1
else:
    print("sorry, you are fail.")
        



