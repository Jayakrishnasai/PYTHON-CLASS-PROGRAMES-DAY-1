def isHappyNumber(num):    
    rem = sum = 0;       
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
num =int(input("enter the number: "))   
result = num;    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result);     
if(result == 1):    
    print(str(num) + " is a happy number");
elif(result < 0):
    print(" not a happy number or invalid ")
elif(result == 4):    
    print(str(num) + " is not a happy number");  
