

dp = [0]*10
dp[0] = 2

print(" dp -> ", dp)


for i in range(len(dp)):
    if dp[i] == 0:
        break
        # continue
else:
    print(" printint in else block after break, no If ")


