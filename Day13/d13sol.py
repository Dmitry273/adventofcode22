packets = [i[:-1] for i in open('Day13/d13.txt', 'r')]

def com(l, r):
    for i in range(min(len(l), len(r))):
        if l[i] != r[i]:
            if type(l[i]) is int and type(r[i]) is int: return l[i] < r[i]
            if type(l[i]) is list and type(r[i]) is list: return com(l[i], r[i])
            if type(l[i]) is list: return com(l[i], [r[i]])
            if type(r[i]) is list: return com([l[i]], r[i])
    else:
        if len(l) != len(r): return len(l) < len(r)
    pass

def comp(left, right):
    while left and right:
        l = left.pop(0)
        r = right.pop(0)
        if l != r:
            if type(l) is int and type(r) is int: return l < r
            if type(l) is list and type(r) is list: return com(l, r)
            if type(l) is list: return com(l, [r])
            if type(r) is list: return com([l], r)
    else:
        if left and not right: return False
        if right and not left: return True

answ = 0
for i, (a, b) in enumerate(zip(packets[0::3],packets[1::3])):
    left = eval(a)
    right = eval(b)
    if comp(left, right): answ += i+1

print(answ)

a = '[[2]]'
b = '[[6]]'

A = 1
for packet in (packets[0::3]+packets[1::3]+[b]):
    right = eval(a)
    left = eval(packet)
    if comp(left, right): A += 1
print(A)
B = 1
for packet in (packets[0::3]+packets[1::3]+[a]):
    right = eval(b)
    left = eval(packet)
    if comp(left, right): B += 1
print(B)
print(A*B)

