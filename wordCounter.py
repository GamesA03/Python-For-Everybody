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

#Find the most common word
largest = -1
word = None
for k,v in di.items() :

    if v > largest:
        largest = v
        word = k #capture/remember the word that was the largest
print('Done',word, largest)