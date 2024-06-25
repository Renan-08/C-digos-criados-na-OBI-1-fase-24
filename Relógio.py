H = int(input())
M = int(input())
S = int(input())
T = int(input())

S += T

if S >= 60:
    M += S //60
    S = S % 60
    
if M >= 60:
    H += M // 60  
    M = M % 60

if H >= 24:
    H = H %24

print(H)
print(M)
print(S)
    
    # TODO: write code...