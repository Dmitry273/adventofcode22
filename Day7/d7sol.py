directories = [{},'.',{}]
curr = directories

for line in open('Day7/d7.txt', 'r'):
    comm = line[:-1]
    if comm[0:1] == '$':
        if comm[2:4] == 'cd':
            if comm[5:] == '/':
                curr = directories
                continue
            elif comm[5:] == '..':
                curr = curr[1]
            else:
                curr = curr[0][comm[5:]]
    else:
        if comm[0:3] == 'dir':
            curr[0].update({comm[4:]:[{},curr,{}]})
        else:
            curr[2].update({comm.split()[1]:int(comm.split()[0])})

answ1 = 0

def weight(node):
    global answ1
    if not node: return 0
    answ = sum(node[2].values())
    for direct in node[0]:
        local = weight(node[0][direct])
        if local <= 100000: answ1 += local
        answ += local
    return answ

weight(directories)
print(answ1)