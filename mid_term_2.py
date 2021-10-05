#while i = true the loop keeps running.:
#    checks if the x in ranges and sees where it is in range for a month
#    then a print statement prints out the date and where the day is the remainder is taken away
#    if user enters a negative number then i = fasle and lexit 





print("Program to calculate the date, month and year in the 2021-2022 academic year of a given day.")

i = 1

while(i):
    x = int(input("Enter the day for which you want to find the date (an integer):"))
    if x<=0:
        print("Finished")
        i=0
    if x >= 366:
        print("Day number" +str(x) +" is not in the 2021-2022 academic year!")
    if x>=1 and x <=31:
        print("Day number "+ str(x) +  " is "+ str(x) +" August 2021")
    if x>31 and x <=61:
        print("Day number "+ str(x) +  " is "+ str(x-31) +" September 2021")
    if x>61 and x <=92:
        print("Day number "+ str(x) +  " is "+ str(x-61) +" October 2021")        
    if x>92 and x <=122:
        print("Day number "+ str(x) +  " is "+ str(x-92) +" November 2021")     
    if x>122 and x <=152:
        print("Day number "+ str(x) +  " is "+ str(x-122) +" December 2021")     
    if x>152 and x <=184:
        print("Day number "+ str(x) +  " is "+ str(x-152) +" January 2021") 
    if x>184 and x <=212:
        print("Day number "+ str(x) +  " is "+ str(x-184) +" Febuary 2021") 
    if x>212 and x <=243:
        print("Day number "+ str(x) +  " is "+ str(x-212) +" March 2021") 
    if x>243 and x <=273:
        print("Day number "+ str(x) +  " is "+ str(x-243) +" April 2021")     
    if x>273 and x <=303:
        print("Day number "+ str(x) +  " is "+ str(x-273) +" May 2021")   
    if x>303 and x <=333:
        print("Day number "+ str(x) +  " is 31 June 2021")
    if x>333 and x <365:
        print("Day number "+ str(x) +  " is "+ str(x-334) +" July 2021")#
    if x == 365: print("Day number "+ str(x) +  " is "+ str(x-334) +" July 2021")
    
        