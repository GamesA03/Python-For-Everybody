fh = open('mbox-short.txt.txt')

for line in fh:
    newLine = line.rstrip()
    #print(newLine.upper())
    wds = line.split()
    #Guardian w/single statement
    if len(wds) < 3:
        continue
    #Guardian w/compound statement
    #if len(wds) < 3 or wds[0] != 'From' :
        #continue
    if wds[0] != 'From':
        continue
    print(wds[2])