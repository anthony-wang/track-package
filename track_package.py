import urllib
import webbrowser
import time

# enter webpage to check - canada post with your tracking info
webpage_tracker = "https://www.canadapost.ca/cpotools/apps/track/personal/findByTrackNumber?trackingNumber=NNNNNNNNNNNNNNNN&LOCALE=en"
# enter the webpage to open when package is attempted or delivered
webpage_music = "https://www.youtube.com/watch?v=IAISUDbjXj0"
# how often to check (seconds)
check_period = 15

#def check_canada_post(url):
flag = False
connection = urllib.urlopen(webpage_tracker)
output = connection.read()
while flag != True:
    if "attempted" in output:
        print time.ctime() + " : Package Delivery Attempted"
        flag = True
        webbrowser.open(webpage_music)
    elif output.count("delivered") > 3:
        print time.ctime() + " : Package Delivered"
        flag = True
        webbrowser.open(webpage_music)
    else:
        print time.ctime() + " : Package in Transit"
        flag = False
    connection.close()
    time.sleep(15)

#check_canada_post(webpage_tracker)