#psueodcode:
#    user enters int
#    if less than 0 -> exit
    
#    if not then enters while loop:
#        if remainder when divisible by 4,5,7,13 == increment counter by 1


print("Program to calculate the number of integers evenly divisible by 4, 5, 7 and 13")
x = int(input(("Enter a non-negative integer:  ")))
if x < 0:
    print("Negative number entered. Error")
    quit()
else: print("You entered: " + str(x))

i = 1
#initilising counters 
c1 = 0
c2 = 0 
c3 = 0
c4 = 0 


while i <= x:
    if i%4==0:
        c1+=1
    if i%5==0:
        c2+=1
    if i%7==0:
        c3+=1
    if i%13==0:
        c4+=1
    i +=1

print("Number of numbers up to and including " +str(x) + " evenly divisible by 4: " + str(c1))
print("Number of numbers up to and including " +str(x) + " evenly divisible by 5: " + str(c2))
print("Number of numbers up to and including " +str(x) + " evenly divisible by 7: " + str(c3))
print("Number of numbers up to and including " +str(x) +  " evenly divisible by 13: " + str(c4))