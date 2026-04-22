import numpy as np

# Տվյալների մուտքագրում
R = [3, 5, 7, 2, 6, 2, 3]
alpha = [3, 5, 4, 3.5, 4.5, 2.5, 4]
n = 7
C1_max = 40
C2_max = 15

# Եկամտի ֆունկցիան
def income_func(j, x, y):
    # Եթե x<=0, այն ոչ իրական է
    if x <= 0:
        return -np.inf  # DP-ն երբեք չի ընտրի
    return R[j] * (1 - np.exp(-alpha[j] * (x + y)))**x

# DP աղյուսակ. dp[փուլ][ռեսուրս1][ռեսուրս2]
dp = np.zeros((n + 1, C1_max + 1, C2_max + 1))
best_x = np.zeros((n, C1_max + 1, C2_max + 1))
best_y = np.zeros((n, C1_max + 1, C2_max + 1))

# Դինամիկ ծրագրավորում (առաջ՝ առաջին արտադրությունից մինչև վերջինը)
for j in range(n):  # 0-ից n-1
    for c1 in range(C1_max + 1):
        for c2 in range(C2_max + 1):
            max_val = -1
            # x սկսում ենք 1-ից, որպեսզի չհաշվի x=0
            for x in range(1, c1 + 1):
                for y in range(c2 + 1):
                    prev = dp[j-1][c1-x][c2-y] if j > 0 else 0
                    current_income = income_func(j, x, y) + prev
                    if current_income > max_val:
                        max_val = current_income
                        best_x[j][c1][c2] = x
                        best_y[j][c1][c2] = y
            dp[j][c1][c2] = max_val

# Արդյունքների վերականգնում
res_x = []
res_y = []
rem_c1, rem_c2 = C1_max, C2_max

for j in reversed(range(n)):
    x_opt = int(best_x[j][rem_c1][rem_c2])
    y_opt = int(best_y[j][rem_c1][rem_c2])
    res_x.append(x_opt)
    res_y.append(y_opt)
    rem_c1 -= x_opt
    rem_c2 -= y_opt

# Քիչ փոփոխություն՝ ռեզուլտը ճիշտ հերթով
res_x.reverse()
res_y.reverse()

print(f"Առավելագույն գումարային եկամուտ: {dp[n-1][C1_max][C2_max]:.2f}")
print("Ռեսուրսների բաշխում (x):", res_x)
print("Ռեսուրսների բաշխում (y):", res_y)