number = list(range(1,10001))
temp = []
for i in number:
    for n in str(i):
        i += int(n)
    if i <= 10000:
        temp.append(i)
for k in set(temp):
    number.remove(k)
for l in number:
    print(l)
