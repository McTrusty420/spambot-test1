try :
    import pyautogui, time, re
except :
    print("pyautogui is missing")
a=input("string")
b=int(input("repetition"))
c=int(input("sleep time"))
d=input("separator")
if a == "file[s]":
    g=input("path/filename")
time.sleep(c)
for i in range(1,b+1):
    if a == "file[s]":
        e=open(g,"r",encoding="UTF-8")
        for j in e :
            h=re.split(d,j)
        for s in h:
            pyautogui.typewrite(s)
            pyautogui.press("enter")
    else:
        f=re.split(d,a)
        for s2 in f:
            pyautogui.typewrite(s2)
            pyautogui.press("enter")