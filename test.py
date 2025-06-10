t = int(input())
for _ in range(t):
    n = int(input())
    if n>=7:
        print("HEAVY")
    elif n>=3 and n<7:
        print("MODERATE")
    elif n <=3:
        print("LIGHT")