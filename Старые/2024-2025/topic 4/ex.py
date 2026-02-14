def dec_to_bin(n): 
    if n == 0:
        return 0
    
    bin = ""
    while n > 0:
        per = n % 2 
        bin = str(per) + bin 
        n = n//2 
    return bin 

print(dec_to_bin(25))
print(dec_to_bin(2))
print(dec_to_bin(10))
print(dec_to_bin(13))




