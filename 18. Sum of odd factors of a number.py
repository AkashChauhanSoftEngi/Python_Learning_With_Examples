def special_func(num):
    total = 0
    a = 0
    if type(num) != int or num < 0:
        return -10
    
    else:
        for i in range(1,num+1,1):
            if num%i == 0 and i%2 !=0:
                total = total + i
            else:
                continue
        return total
  

print(special_func(12))
