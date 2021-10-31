import random

def sosubango(ina):
    x,li = 1,[]
    for k in range(max(ina)):
        while True:
            x, sh = x + 1, 0
            for i in range(x-2):
                if x % (i+2) == 0:
                    sh = i + 2
                    break
            if sh == 0: break
        for i in range(len(ina)):
            if ina[i] == k + 1:
                li.append(x)
                print("["+str(len(li))+"/"+str(len(ina))+"]  "+str(k+1)+" 番目の素数を求めています。")
    return li

def angoka(x,y):
    out,rand = 1,[]
    for i in range(y):
        rand.append(random.randint(1,x-1))
    rand.append(x)
    li = sosubango(rand)
    for i in range(len(li)-1):
        out = out * (li[i]**2)
    out = out * li[-1]
    return out

if __name__ == __main__:
    x = int(input("暗号化する数 > "))
    y = int(input("暗号化の強さ(1以上) > "))
    print("\n "+str(angoka(x,y))+"\n")
