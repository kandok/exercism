def is_armstrong_number(number):
    n = number
    b = len(str(n))
    sum1 = 0
    
    while n != 0:
        r = n % 10
        sum1 = sum1+(r**b)
        n = n//10
        
    return number == sum1
