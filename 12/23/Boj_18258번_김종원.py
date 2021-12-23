# 큐2

class qu:
    def __init__(self):
        self.x = []

    def push_X(self,num):
        self.x.append(num)

    def pop(self):
        if len(self.x)==0:
            return -1
        else:
            return self.x.pop(0)
    def empty(self):
        if len(self.x) ==0:
            return 1
        else:
            return 0

    def size(self):
        return len(self.x)

    def front(self):
        if len(self.x)==0:
            return -1
        else:
            return self.x[0]
    def back(self):
        if len(self.x) ==0:
            return -1
        else:
            return self.x[-1]


q = qu()
n = int(input())
# print(n)
comands = []
for i in range(n):
    comand = input()
    comands.append(comand)

for c in comands:
    cs = c.split()
    if cs[0] =="push":
        q.push_X(int(cs[1]))
    elif cs[0] =="front":
        print(q.front())
    elif cs[0] == 'back':
        print(q.back())
    elif cs[0] =='size':
        print(q.size())
    elif cs[0] == 'pop':
        print(q.pop())
    elif cs[0] == 'empty':
        print(q.empty())