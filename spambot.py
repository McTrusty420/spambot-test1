try :
    import pyautogui, time, re
except :
    print("pyautogui is missing")
spam_input=input("string")
repetition=int(input("repetition"))
time_interval=int(input("sleep time"))
separator=input("separator")
split_text=""
if spam_input == "file":
    file=input("path/filename")
time.sleep(time_interval)
for reps in range(1,repetition+1):
    if spam_input == "file":
        file_opened=open(file,"r",encoding="UTF-8")
        for split_words in file_opened :
            split_text=re.split(separator,)
        for words in split_text:
            pyautogui.typewrite(words)
            pyautogui.press("enter")
    else:
        final_string=re.split(separator,spam_input)
        for spam in final_string:
            pyautogui.typewrite(spam)
            pyautogui.press("enter")
