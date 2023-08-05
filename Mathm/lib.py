def A(m,n): 
    if (m==1):
        return n
    else:
        return n*A(m-1,n-1)
def C(m,n):
    return A(m/n)/A(m,m)
def factor(num):
    ans = []
    for i in range(1,num+1):
        if (num%i==0):
            ans.append(i)
    return ans
def gcd(n,m):
    if n<m:
        n,m=m,n
    if n%m==0:
        return m
    else:
        return gcd(m,n%m)
def lcm(n,m):
    return (n*m/gcd(n,m))
def isPrime(num):
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                return False
        else:
            return True
    else:
        return False
def findprimes(num):
    ans = []
    for i in range(1,num+1):
        if isPrime(i):
            ans.append(i)
    return ans
def rounding(num, n):
    if '.' in str(num):
        if len(str(num).split('.')[1]) > n and str(num).split('.')[1][n] == '5':
            num += 1 * 10 ** -(n+1)
    if n:
        return round(num, n)
    else:
        return round(num)
def reciprocal(a):
    return 1/a

def powm(a,m):
    x = a; n = m; y = 1        
    while n:                
        if n == 0:          
            break
        else:
            if n %2 == 0:       
                x = x * x
                n = n / 2
            else:               
                y = x * y
                n = n - 1
    return y
def sqrt(num):
    return num**0.5