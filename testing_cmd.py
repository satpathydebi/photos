#import pywhatkit as kit
#from datetime import datetime, timedelta
#import pyautogui
#import time
#
## Replace these values with your information
#phone_number = "+919986426100"  # Include your country code
#message = "Hello, this is a test message!"
#
## Set the time for the message to be sent
#now = datetime.now()
#hours = now.hour
#minutes = now.minute + 1  # Message will be sent 2 minutes from now
#
## Open WhatsApp Web
#kit.open_web()
#
## Wait for WhatsApp Web to open (adjust the sleep duration if needed)
#time.sleep(10)
#
## Type the phone number and press Enter
#pyautogui.write(phone_number)
#pyautogui.press("enter")
#
## Wait for the chat to open (adjust the sleep duration if needed)
#time.sleep(5)
#
## Type the message and press Enter
#pyautogui.write(message)
#pyautogui.press("enter")
#
## Close the browser (you may need to adjust the sleep duration based on your system)
#time.sleep(5)
#pyautogui.hotkey('ctrl', 'w')
#
## Wait for the browser to close (adjust the sleep duration if needed)
#time.sleep(5)
#
## Close the WhatsApp Web tab
#pyautogui.hotkey('ctrl', 'w')
#
## Wait for the tab to close (adjust the sleep duration if needed)
#time.sleep(5)
#

#strt="infrastructure"
#newstr=""
#d_newstr=""
#l=[]
#for i in strt:
#    val=strt.count(i)
#    newstr+=i
#    if val >1:
#        #print(val)
#        d_newstr=str(val)
#        #l.append(newstr)
#        newstr+=d_newstr
#        #print(i)
#        newstr.strip(i)
#
#desired="I N F 3R A S 2T 2U C E"
#
#
##a={
##	"a": 1,
##	"b": 2,
##	"c": [{"d": 3, "e": 4},{"f": 3, "g": 4}],
#	"h": 5
#}
#for key,value in a.items():
#    #print(key)
#    if value == 4:
#        print(key)
#    else:
#        if type(value) is list:
#            for j in value:
#                for key,val in j.items():
#                    if val == 4:
#                        print(key)
                
word_t='bunty'
x=' '.join(word[::-1] for word in word_t.split())
print(x)

