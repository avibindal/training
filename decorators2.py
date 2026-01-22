def triple(oldfunc):
    def newfunction(m):
        m = m+10
        
        return 2*oldfunc(m)
    
    return newfunction

@triple
def square(n):
    return n*n
print(square(5))