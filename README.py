# soft-dirinking
t = int(input())
for _ in range(t):
    n, k, l, c, d, p, nl, np = map(int, input().split())
    t_toasts = (k * l) // nl
    t_limes = c * d
    t_salt = p // np
    every_peron = min(t_toasts, t_limes, t_salt) // n
    print(every_peron)
