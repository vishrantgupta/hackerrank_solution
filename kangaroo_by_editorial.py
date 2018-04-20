# If v1 <= v2, they will never meet.
# We just need to check if a solution exists for the following equation:
#
# x1 + t*v1 == x2 + t*v2
#
# This is equivalent to checking if (x2 - x1) % (v1 - v2) == 0

x1, v1, x2, v2 = map(int, raw_input().split())
X = [x1, v1]
Y = [x2, v2]
back = min(X, Y)
fwd = max(X, Y)
dist = fwd[0] - back[0]

while back[0] < fwd[0]:
    back[0] += back[1]
    fwd[0] += fwd[1]
    if fwd[0] - back[0] >= dist:
        break

print ["NO", "YES"][back[0] == fwd[0]]
