from datetime import *
import webbrowser
import calendar
import sched
import time
from twilio.rest import Client

''' 
This is essentially the same script as main.py but if you have a free Twilio account and would like to get a text message
when it's time for class, you can use this script to do that. You'll have to update your Twilio account sid and auth id accordingly.
'''

bio =   'https://us04web.zoom.us/j/123456789/pwd=?'
phys = ''
maths = ''
eng =''
chem = ''

today_date = str(date.today())
day_of_week = calendar.day_name[date.today().weekday()]

'''Change the contents of this dictionary (time table) accordingly.''' 

class_times ={
    'Monday':[['09 30',bio],['10 30',maths],['11 30',eng],['12 30',chem],['14 10',phys]],
               'Tuesday':[['09 30',bio],['10 30',chem],['11 30',maths],['12 30',chem],['14 10',eng]],
               'Wednesday':[['09 30',phys],['10 30',maths],['11 30',bio],['12 30',chem],['14 10',eng]],
               'Thursday':[['09 30',phys],['10 30',eng],['11 30',maths],['12 30',chem],['14 10',bio]],
               'Friday':[['09 30',chem],['10 30',bio],['11 30',maths],['12 30',phys],['14 10',eng]],
    'Saturday':[['09 30',chem],['10 30',bio],['11 30',maths],['12 30',eng],['14 10',phys]]
    }


'''
Update your Twilio credentials here.
'''

account_sid = 'sample'
auth_token = 'sample'
my_cell = 'yourphone'
my_twilio = 'sample'
my_msg = "Time for class"

'uncomment this line'
#client = Client(account_sid,auth_token)			

x= sched.scheduler(time.time,time.sleep)

def zoom_class(link):
        webbrowser.open(link)
        'uncomment this line'
        #message = client.messages.create(to = my_cell, from_ =my_twilio, body = my_msg )
        
def get_new_time(old_time):
    added_minutes=int(old_time[3:]) + 40
    if added_minutes >= 60:
        new_time = str(str(int(old_time[:2]) + 1) + ' ' + str(added_minutes - 60))
    else:
        new_time = str(old_time[:2]) + ' ' + str(added_minutes)

    return new_time
    
    
def attend():
    if day_of_week in class_times.keys():
        class_no = 0 #this is for the loop
        
        for i in range(5):
            if time.strptime(f'{today_date} {class_times[day_of_week][class_no][0]}','%Y-%m-%d %H %M') > time.localtime():
                x.enterabs((time.mktime(time.strptime(f'{today_date} {class_times[day_of_week][class_no][0]}',"%Y-%m-%d %H %M"))),0,zoom_class,kwargs={'link':class_times[day_of_week][class_no][1]})
                #to rejoin after 40 mins
                #x.enterabs((time.mktime(time.strptime(f'{today_date} {get_new_time(class_times[day_of_week][class_no][0])}',"%Y-%m-%d %H %M"))),0,zoom_class,kwargs={'link':class_times[day_of_week][class_no][1]})
                class_no +=1        
            else:
                class_no +=1
                
        x.run()
        print("No more classes today!")
                
    else:
        print("NO CLASS FOR TODAY.")

if __name__ == '__main__':
    attend()
