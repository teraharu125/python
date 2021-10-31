def soinsu(x):
    a,y,z,li = 2,x,x,[]
    while (a <= y):
        z = z % a
        if z == 0:
            print (a, " - " ,y)
            li.append(a)
            z = y // a
            y = z
        z = z % a
        if z >= 1:
            z,a = y,a + 1
    return li

def hitotsu(x):
    for i in range(int((len(x)-1)/2)):
        if x[2*i] != x[2*i+1]:
            return x[2*i]
    return x[len(x)-1]

def nanbanme(ina):
    x,m = 1,0
    while True:
        x, sh = x + 1, 0
        for i in range(x-2):
            if x % (i+2) == 0:
                sh = i + 2
                break
        if sh == 0:
            m = m + 1
            if ina == x: break
    return m

while True:
    x = int(input(" > "))
    print("\n結果:   "+str(nanbanme(hitotsu(soinsu(x))))+"\n")