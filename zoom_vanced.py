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
        
def second(old_time, add):
    sec = time.mktime(old_time) + (add*60)
    return datetime.fromtimestamp(sec)

def attend():
        late = True
        if day_of_week in class_times.keys():            
                for i in class_times[day_of_week]:                        
                        timing_str = time.strptime(f'{today_date} {i[0]}','%Y-%m-%d %H %M')
                        second_timing = time.strptime(f'{second(timing_str,add=i[1][1])}',"%Y-%m-%d %H:%M:%S")
                                                
                        if timing_str > time.localtime() and i[1] not in cancel:
                                x.enterabs((time.mktime(timing_str)),0,zoom_class,kwargs={'link':i[1][0]})
                                #to rejoin for second sess
                                x.enterabs((time.mktime(second_timing)),0,zoom_class,kwargs={'link':i[1][0]})

                        elif timing_str < time.localtime() and i[1] not in cancel and late:
                            if time.mktime(time.localtime()) - time.mktime(timing_str) < (12*60):
                                webbrowser.open(i[1][0])
                                x.enterabs((time.mktime(second_timing)),0,zoom_class,kwargs={'link':i[1][0]})
                                
                            elif second_timing > time.localtime():
                                x.enterabs((time.mktime(second_timing)),0,zoom_class,kwargs={'link':i[1][0]})
                                
                            else:
                                pass
                      
                        else:
                                pass
                
                x.run()
                
    else:
        print("NO CLASS FOR TODAY.")

if __name__ == '__main__':
    attend()
