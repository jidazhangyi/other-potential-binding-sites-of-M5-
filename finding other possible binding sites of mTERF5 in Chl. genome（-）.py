#finding other possible binding sites of mTERF5 in Chl. genome
#input the genome sequence of Chl. #
f = open("c:/a.seq", "r")  
m = []
n = []
x = []
for eachLine in f:
    line1=eachLine.strip()
    a=list(line1)
    for i in a:
        m.append(i)
for j in range(len(m)-21):
    for i in range(21):
        n.append(m[j+i])
    x.append(''.join(n))
    n = []
# revise the list using 21 nt M5 binding sequence
m5s=['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
l = 0
for x1 in x:
    b = list(x1)
    for b1 in b:
        n.append(b1)
    for z in range(21):
        if m5s[z]==n[z]:
            l +=1
        else:
            l=l
# the number for mismatch
    if l > 13:
        print ''.join(n)
    else:
        pass
    n = []
    l = 0
print 'finished'
f.close()
