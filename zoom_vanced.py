from datetime import date
import webbrowser
import calendar, sched
import time
from twilio.rest import Client



bio =   'https://us04web.zoom.us/j/123456789/pwd=?'
phys = ''
maths = ''
eng =''
chem = ''

'''Change the contents of this dictionary (time table) accordingly.''' 

class_times ={
    'Monday':[['09 00',phys],['10 15',maths],['11 30',bio],['13 15',chem],['14 30',phys]],

               'Tuesday':[['09 00',phys],['10 15',eng],['11 30',bio],['13 15',chem],['14 30',maths]],

               'Wednesday':[['09 00',bio],['10 15',phys],['11 30',maths],['13 15',chem],['14 30',bio]],

               'Thursday': [['09 00',maths],['10 15',chem],['11 30',maths],['13 15',bio],['14 30',phys]],

               'Friday':[['09 00',bio],['10 15',chem],['11 30',phys],['13 15',maths],['14 30',chem]],

    'Saturday':[['09 00',phys],['10 15',eng],['11 30',bio],['13 15',chem],['14 30',maths]]
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

today_date = str(date.today())
day_of_week = calendar.day_name[date.today().weekday()]

x= sched.scheduler(time.time,time.sleep)

def zoom_class(link):
        webbrowser.open(link)
        'uncomment this line'
        #message = client.messages.create(to = my_cell, from_ =my_twilio, body = my_msg )
        
def get_new_time(old_time, add):
    added_minutes=int(old_time[3:]) + add
    if added_minutes >= 60:
        new_time = str(str(int(old_time[:2]) + 1) + ' ' + str(added_minutes - 60))
    else:
        new_time = str(old_time[:2]) + ' ' + str(added_minutes)

    return new_time
    
    
def attend():
    if day_of_week in class_times.keys():
        class_no = 0 #this is for the loop
        
        for i in class_times[day_of_week]:
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
