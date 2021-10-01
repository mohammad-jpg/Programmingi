Leinster = ["dublin" , "kilkenny" , "waterford"]
Ulster = ["belfast" , "derry" , "lisburn"]
Connacht = ["galway" , "sligo"]
Munster = ["cork" , "limerick"]
input = str(input("Please enter town name: "))

if input.lower() in Leinster:
    print("You entered "+ input + ". " + input+" is in Leinster")
elif input.lower() in Munster:
    print("You entered "+ input + ". " + input+" is in Munster")
elif input.lower() in Connacht:
    print("You entered "+ input + ". " + input+" is in Connacht")
elif input.lower() in Ulster:
    print("You entered "+ input + ". " + input+" is in Ulster")
else:
    print("Sorry Didnt recognize the name")