data = ''
with open('test.txt', 'r') as f:
    data = f.read()

data = data.strip()

groups = data.split('\n\n')

for i in range(len(groups)):
    groups[i] = groups[i].split('\n')

sums = []

for group in groups:
    group = [int(x) for x in group]
    inner_sum = sum(group)
    sums.append(inner_sum)

max = max(sums)
print(max)

sums.sort(reverse = True)
top3 = sums[:3]
print(sum(top3)) 