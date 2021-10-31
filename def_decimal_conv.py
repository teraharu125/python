"""
x : decimal
y : radix
"""
def decimal_conv(x,y):
    x,y,lis,out,alpha = int(x),int(y),[],"",[chr(i) for i in range(65,65+26)]
    while x>=y:
        lis.append(x%y)
        x = int((x-(x%y))/y)
    lis.append(x)
    for i in range(len(lis)):
        for k in range(len(alpha)):
            if lis[len(lis)-i-1] == k+10: lis[len(lis)-i-1] = alpha[k]
        out = out+str(lis[len(lis)-i-1])
    return out

if __name__ == __main__:
    x = input("10進数の数字を入力 > ")
    y = input("変換後の進数を入力 > ")
    print(decimal_conv(x,y))
