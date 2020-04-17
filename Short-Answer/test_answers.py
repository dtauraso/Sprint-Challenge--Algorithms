def problem1(n):
    a = 0
    count = 0
    while (a < n * n * n):
        print(count, a)
        a = a + n * n
        count += 1
def problem2(n):
    sum = 0
    count2 = 0
    for i in range(n): # n as i goes from 0 to n
        print(count2)

        j = 1
        count2 += 1
        count1 = 0
        while j < n: # log(n)  as j doubles each time
            print(" ", count1)

            j *= 2
            sum += 1
            count1 += 1


# problem1(20)

problem2(16)


