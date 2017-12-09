# time_zone ='xxx'
# init_command='SET time_zone = "%s"' % time_zone
# print init_command
# 
# 
# 'xxyz'
# 1+1


from threading import Timer  
import time  
  
timer_interval=10  

class person():
    def __init__(self,name):
        self.name=name
        
    def say(self):  
        print 'i m ',self.name  

person=person('wxf')

t=Timer(timer_interval,person.say())  
t.start() 
t.setDaemon(True)
