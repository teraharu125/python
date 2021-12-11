import winsound
from time import sleep
def write(file_name,alert):
    with open("Data.txt","w") as f:
        print(file_name+"\n"+str(alert),file=f)
with open("Data.txt","r") as g:
    data = g.readlines()
file_name = data[0].replace("\n","")
if str.isdecimal(data[1].replace("\n","")): alert = int(data[1].replace("\n",""))
else:
    alert = 5
    write(file_name,5)
    print("Data.txtのエラーを検出しました。アラート回数をリセットしました。")
print("filename: "+file_name+"\nalert_time: "+str(alert))
while True:
    x,k = input(" > "),0
    for i in x.split():
        if str.isdecimal(i): k+=1
        else: break
    if k==len(x.split()) and len(x.split())<4: break
    elif x=="help": print("数字を入力でタイマー開始\n「6」→ 6分、「0 25」→ 25秒、「1 30 00」→ 1時間30分\n\nsettings music [filename] で音声ファイル変更(waveファイルのみ)\nsettings alert [回数] で再生回数変更\nreset リセット\nshow ステータスを表示")
    elif x.split()[0]=="settings":
        if x.split()[1]=="music" and len(x.split())==3:
            file_name = x.split()[2]
            print("ファイル名変更完了")
        elif x.split()[1]=="alert" and len(x.split())==3 and str.isdecimal(x.split()[2]):
            alert = x.split()[2]
            print("アラート回数変更完了")
        write(file_name,alert)
    elif x.split()[0]=="reset":
        write("default.wav",5)
        print("リセット完了")
    elif x.split()[0]=="show": print("filename: "+file_name+"\nalert_time: "+str(alert))
    else: print("対応した型で入力してください")
sec = [int(i.split()[0])*60 if len(i.split())==1 else int(i.split()[0])*60+int(i.split()[1]) if len(i.split())==2 else int(i.split()[0])*3600+int(i.split()[1])*60+int(i.split()[2]) for i in [x]][0]
for i in range(sec):
    print("Times Remain: "+str(int(((sec-i)-((sec-i)%3600))/3600))+"h "+str(int(((sec-i)%3600-((sec-i)%60))/60))+"m "+str((sec-i)%60)+"s")
    sleep(1)
print("TImes Up")
for i in range(alert):
    winsound.PlaySound("music/"+file_name, winsound.SND_FILENAME)
    print("残り "+str(alert-1-i)+" 回再生")