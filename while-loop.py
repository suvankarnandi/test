
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


mobile = (8443910056, 9674423685, 9239417975, 8240129420, 9239381348 )

number = int(input("put your number:"))
id = 0
while id < len(mobile):
    if (mobile[id] == number):
        print("found your number in the list ", id)
        break

    else: 
        print ("number not listed.")
    id +=1
    



