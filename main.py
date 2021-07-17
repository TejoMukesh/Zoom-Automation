from datetime import date
import webbrowser
import calendar
import sched
import time

eng =   'https://us04web.zoom.us/j/123456789'
maths = 'link'
phys = 'link'
bio ='link'
chem = 'link'

class_times ={
    'Monday':[['09 30',bio],['10 30',maths],['11 30',eng],['12 30',chem],['14 10',phys]],
               'Tuesday':[],
               'Wednesday':[],
               'Thursday':[],
               'Friday':[],
    'Saturday':[]
    }

today_date = str(date.today())
day_of_week = calendar.day_name[date.today().weekday()]
x= sched.scheduler(time.time,time.sleep)

def get_new_time(old_time):
    added_minutes=int(old_time[3:]) + 40
    if added_minutes >= 60:
        new_time = str(str(int(old_time[:2]) + 1) + ' ' + str(added_minutes - 60))
    else:
        new_time = str(old_time[:2]) + ' ' + str(added_minutes)

    return new_time
    
def attend():
    if day_of_week in class_times.keys():
                
        for i in class_times[day_of_week]:
            if time.strptime(f'{today_date} {class_times[day_of_week][class_no][0]}','%Y-%m-%d %H %M') > time.localtime():
                x.enterabs((time.mktime(time.strptime(f'{today_date} {i[0]}',"%Y-%m-%d %H %M"))),0,webbrowser,kwargs={'url':i[1]})
                #to rejoin after 40 mins
                x.enterabs((time.mktime(time.strptime(f'{today_date} {get_new_time(i[0])}',"%Y-%m-%d %H %M"))),0,webbrowser,kwargs={'url':i[1]})
                pass  
            else:
                pass
                
        x.run()
        print("No more classes today!")
                
    else:
        print("NO CLASS FOR TODAY. Chill.")

if __name__ == '__main__':
    attend()
