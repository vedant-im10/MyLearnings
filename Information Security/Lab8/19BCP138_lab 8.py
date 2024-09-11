from decimal import Decimal 

def gcd(m,n): 
    if n==0: 
        return m 
    return gcd(n,m%n) 
    
#input variables
p = 11
q = 13
    
no = float(input("Enter your message: "))

#calculate n
n = p*q
 
#calculate totient
totient = (p-1)*(q-1) 

#calculate K
for k in range(2,totient): 
    if gcd(k,totient)== 1: 
        break
  
for i in range(1,10): 
    x = 1 + i*totient 
    if x % k == 0: 
        d = int(x/k) 
        break


local_cipher = Decimal(0) 
local_cipher = pow(no,k) 
cipher_text = local_cipher % n 

decrypt_t = Decimal(0) 
decrypt_t= pow(int(cipher_text),d) 
decrpyted_text = float(decrypt_t % n) 
  
print('\n'+'n = ',str(n))
print('k = ',k)
print('totient = ',totient)
print('d = ',d) 
print('cipher text = ',cipher_text)
print('decrypted text = ',decrpyted_text)