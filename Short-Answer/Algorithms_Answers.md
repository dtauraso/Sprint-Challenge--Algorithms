#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    a = 0
    while (a < n * n * n):
      a = a + n * n

    O(n) time
    a = a + n^2 each time
    a + n^2, (a + n^2) + n^2, ((a + n^2) + n^2) + n^2

    we are adding n^2 n times = n^2 * n = n^3 to reach  n * n * n

b)
    sum = 0
    for i in range(n): n as i goes from 0 to n
      j = 1
      while j < n: // log(n)  as j doubles each time
        j *= 2
        sum += 1
    total time is O(nlog(n))
    for each i in n
        double j each time till it reaches n(log(n))
c)
    if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

    O(n):
    each recursive call we subtract 1 off bunnies

## Exercise II

prompt
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

O(log(n))
assume all eggs are created with the same method(no random cheat prepared eggs)
drop from story n
if it doesn't break:
    return true
else:

    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2

        drop from mid building
        if it breaks
            if(high - 1 == low)
                return low # is this the largest possible story?
            high = mid - 1
        elif if doens't break
            # last round
            if(low + 1 == high)
                return low  # this should be the largest story it doesn't break on
                            # if we continue the egg is likely to break

            low = mid + 1
        get another egg

