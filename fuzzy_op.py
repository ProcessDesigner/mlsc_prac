A = [[1,0.1],[2,0.2]]
B = [[4,0.5],[5,0.3],[6,0.7]]

A = dict(A)
B = dict(B)

U = sorted(set(A)|set(B))

union = []
intersection = []
alg_sum = []
set_diff = []
bound_sum = []
bound_diff = []

for x in U:
    a = A.get(x,0)
    b = B.get(x,0)

    union.append([x,a if a>b else b])
    intersection.append([x,a if a<b else b])
    alg_sum.append([x,a+b-a*b])
    set_diff.append([x,a*(1-b)])
    bound_sum.append([x,1 if a+b>1 else a+b])
    bound_diff.append([x,0 if a+b<1 else a+b-1])

print("Union:",union)
print("Intersection:",intersection)
print("Algebric SUm:",alg_sum)
print("Set Difference:",set_diff)
print("Bounded Sum:",bound_sum)
print("Bounded Difference:",bound_diff)
