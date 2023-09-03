# Lothar Colltaz formulae

c0 = int(input("Enter number:- "))

count = 0

while c0 != 1:

    count += 1
#if even
    if c0 % 2 == 0:

        c0 = c0 // 2
#if odd
    elif c0 % 2 == 1:

        c0 = c0*3 + 1

    print(c0)

else:

    print("steps = ", count)
