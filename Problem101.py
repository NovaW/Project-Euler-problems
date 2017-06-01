def u(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def OP(S,k,n): #S is the sequence
    i = 0
    XY = []
    while i < k:
        XY.append([i+1,S[i]])
        i += 1
    return Lagrange(XY,n)


def Lagrange(XY, x):    #XY is a list of K points (Kx2 array of values), this uses lagrange interpolation
    K = len(XY)         # on those points and evaluates the resulting polynomial at x
    Lx = 0
    for j in range(K):
        lj  = 1
        for m in range(K):
            if m==j:
                continue
            lj *= (x - XY[m][0])/(XY[j][0]-XY[m][0])
        Lx += XY[j][1]*lj
    return Lx

def main():
    N = 10 # degree of the polynomial u(n)
    S = []
    for i in range(N):
        S.append(u(i+1))
    FITs = []
    for i in range(N):
        FITs.append(OP(S,i+1,i+2))
    sumFITs = sum(FITs,0)
    return(sumFITs)

print(main())