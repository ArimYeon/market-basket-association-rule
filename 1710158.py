import sys
# data 전처리
data = []
i = 0
first = 0
tranCount = 0
file = open(sys.argv[1], 'r')
for line in file:
    tranCount += 1
    first = 1
    for item in line.split(','):
        if first == 1:
            first = 0
            continue
        data.append(item.replace("\n", ""))
    data.append('\n')
#print(data)

# Step 1: Find frequent 1-itemsets
minsup = float(sys.argv[2]) * tranCount
C1 = [0]*100
for item in data:
    if item != '\n':
        C1[int(item)] += 1
#print(C1)
F1 = []
for i in range(100):
    if C1[i] >= minsup:
        F1.append(i)
#print(F1)

# Step 2: Generate candidate 2-itemsets
C2 = []
for i in range(len(F1)):
    for j in range(i+1, len(F1)):
        C2.append([F1[i], F1[j]])
#print(C2)

# Step 3: Find frequent 2-itemsets
F2 = []
a = []
data2 = []
file = open(sys.argv[1], 'r')
for line in file:
    first = 1
    for item in line.split(','):
        if first == 1:
            first = 0
            continue
        a.append(int(item.replace("\n", "")))
    data2.append(a)
    a = []
#print(data2)

count = 0
support = [[0]*100 for i in range(100)]
for tran in data2:
    for c in C2:
        count = 0
        for item1 in c:
            if item1 in tran:
                count += 1
        if count == 2:
            support[c[0]][c[1]] += 1

for i in range(100):
    for j in range(100):
        if support[i][j] >= minsup:
            F2.append([i, j])
#print(F2)

# Step 4: Generate association rules
minconf = float(sys.argv[3])
print("Association rules found:")
for f2 in F2:
    if (support[f2[0]][f2[1]] / C1[f2[0]]) > minconf:
        print(f2[0], "->", f2[1], "( support =", support[f2[0]][f2[1]] / tranCount, ", confidence =", support[f2[0]][f2[1]] / C1[f2[0]], ")")
    if (support[f2[0]][f2[1]] / C1[f2[1]]) > minconf:
        print(f2[1], "->", f2[0], "( support =", support[f2[0]][f2[1]] / tranCount, ", confidence =", support[f2[0]][f2[1]] / C1[f2[1]], ")")
