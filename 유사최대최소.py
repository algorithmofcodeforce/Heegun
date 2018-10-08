a, b = map(int, input().split())
t = min(a, b)
k = max(a, b)
aw = 0
s = []
if k % t == 0:
    aw == t
else:
    for i in range(1, k):
        if t % i == 0 and k % i == 0:
            s.append(i)
    s.sort()
    aw = s[- 1]
lcm = t*k//aw

print(aw)
print(lcm)
