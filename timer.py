from dateutil.relativedelta import relativedelta
from datetime import datetime

import tkinter  as tk 
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("405x170")  
from time import strftime
dt=datetime.today()
# Below line is used for testing by adding 10 seconds to present time
dt2=datetime(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second+10)
def my_time():
    dt=datetime.today()
    # comment the below line to test the script with 10 second gap
    dt2=datetime(dt.year+1,1,1,0,0,0) # Date and time for new year
    dt3=relativedelta(dt2,dt) # time left for new year 
    h=dt3.hours
    m=dt3.minutes
    s=dt3.seconds
    #print(h,m,s)
    if(h>0 or m>0 or s>0):
        t_string = str(h).zfill(2)+ ":" + str(m).zfill(2) +":"+ str(s).zfill(2)
    else:
        l1.config(font=('times',40,'bold'))
        t_string="Happy New Year"
    l1.config(text=t_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',76,'bold') # display size and style

l1=tk.Label(my_w,font=my_font,bg='yellow')
l1.grid(row=1,column=1,padx=5,pady=25)

my_time()
my_w.mainloop()
