"""
This example demonstrates the use of the Redis job store.
On each run, it adds a new alarm that fires after ten seconds.
You can exit the program, restart it and observe that any previous alarms that have not fired yet
are still active. Running the example with the --clear switch will remove any existing alarms.
"""

from datetime import datetime, timedelta
import sys
import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler


class person():
    def __init__(self,name):
        self.name=name
    def say(self):
        print self.name+'xyz'
p=person('wxf')
fun=p.say

def alarm(time):
    print('Alarm! This alarm was scheduled at %s.' % time)
def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_jobstore('redis', jobs_key='example.jobs', run_times_key='example.run_times',host='47.94.206.52',port=6379,password='wxf1983',db=0)
#     scheduler.remove_all_jobs()
    alarm_time = datetime.now() + timedelta(seconds=10)
    #scheduler.add_job(alarm, 'date', run_date=alarm_time, args=[datetime.now()])
    print(datetime.now())
    scheduler.add_job(tick, 'date', run_date=alarm_time)
        
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
   
    