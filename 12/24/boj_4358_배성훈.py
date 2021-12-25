import sys
import time
from collections import defaultdict

start = time.time()

trees = defaultdict(int)

count = 0
for line in sys.stdin:
    if line == "\n":
        break
    tree = line.rstrip()
    count += 1

    trees[tree] += 1

tree_list = list(trees.keys())
tree_list.sort()

for tree in tree_list:
    print("%s %.4f" % (tree, trees[tree] / count * 100))

print(time.time() - start)
