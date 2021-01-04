file = open('temp.txt', 'r')
lines = file.readlines()
file.close

count = 1
temp = []
result = []
for line in lines:
    if count == 9:
        count = 1
        result.append(temp)
        temp = []
    else:
        temp.append(line.strip())
        count +=1

for r in result:
    r[1] = r[1].upper()
    r[2] = r[2].upper()
    r[0], r[1], r[2] = r[1], r[2], r[0]
    if r[3] == 'D':
        r[3] = "Defender"
    elif r[3] == 'M':
        r[3] = 'Midfields'
    elif r[3] == 'F':
        r[3] = 'Attacker'
    else:
        r[3] = 'Goalkeeper'
    r[4], r[7], r[6] = r[6], r[4], r[5]
    r[5] = 'USA'
    r.append('POR')

file2 = open('temp.txt', 'w')
for x in result:
    s = ' '.join(x) + '\n'
    file2.writelines(s)
file2.close()