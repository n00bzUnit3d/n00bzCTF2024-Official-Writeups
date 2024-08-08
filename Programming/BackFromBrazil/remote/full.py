import random, time

def solve(eggs):
    n = len(eggs)
    dp = []

    for i in range(n):
        dp.append([-1] * n)

    dp[0][0] = eggs[0][0]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if i != 0:
                dp[i][j] = dp[i - 1][j]
            if j != 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])

            dp[i][j] += eggs[i][j]

    return dp[-1][-1]

n = 1000

start = time.time()

for _ in range(10):
    eggs = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0, 696969))
            print(row[j], end=' ')
        eggs.append(row)
        print()

    solution = solve(eggs)
    print("optimal: " + str(solution) + " 🥚")
    inputPath = input()
    inputAns = eggs[0][0]
    x = 0
    y = 0

    for direction in inputPath:
        match direction:
            case 'r':
                x += 1
            case 'd':
                y += 1
            case _:
                print("🤔")
                exit()

        if x == n or y == n:
            print("out of bounds")
            exit()

        inputAns += eggs[x][y]



    if inputAns < solution:
        print(inputAns)
        print("you didn't find enough 🥚")
        exit()
    elif len(inputPath) < 2 * n - 2:
        print("noooooooooooooooo, I'm still in Brazil")
        exit()

    if int(time.time()) - start > 30:
        print("you ran out of time")
        exit()

print("tnxs for finding all my 🥚")
f = open("/flag.txt", "r")
print(f.read())
