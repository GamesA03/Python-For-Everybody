fname = input('Enter file: ')
if len(fname) < 1 :
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand: 
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        #idion: retireve/create/update counter
        di[w] = di.get(w,0) + 1
        print(w,'new',di[w])
#print(di)

#x=sorted(di.items())
#print(x[:5])

temp = list()
for k,v in di.items() :
    #print(k,v)
    nuTup = (v,k)
    temp.append(nuTup)
#print("Flipped",temp)
tmp=sorted(temp, reverse=True)
#print("Sorted", tmp[:5])

for v,k in temp[:5] :
    print(k,v)