from pwn import *
from tqdm import tqdm

p = remote("24.199.110.35","43298")

n = 1000

for i in tqdm(range(10)):
    eggs = []
    for i in range(n):
        eggs.append(list(map(int, p.recvline().split())))

    dp = []
    backtrace = []
    for i in range(n):
        dp.append([-1] * n)
        backtrace.append([0] * n)

    dp[0][0] = eggs[0][0]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            down = True


            if i != 0:
                dp[i][j] = dp[i - 1][j]
            if j != 0:
                if dp[i][j] < dp[i][j - 1]:
                    dp[i][j] = dp[i][j - 1]
                    down = False

            dp[i][j] += eggs[i][j]


            backtrace[i][j] = (b"r" if down else b"d")

    ans = b""

    i = n - 1
    j = n - 1

    while i != 0 or j != 0:
        ans = backtrace[i][j] + ans
        if backtrace[i][j] == b"d":
            j -= 1
        else:
            i -= 1


    p.recvuntil(b"optimal")
    p.recvline()
    p.sendline(ans)

p.recvline()
print(p.recvline())
