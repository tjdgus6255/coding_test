H, M = map(int, input().split())

M45 = M - 45
H45 = H

if M45 < 0 :
    M45 = 60 + M45
    H45 = H45 - 1
    if H45 < 0 :
        H45 = 23

print(H45, M45)