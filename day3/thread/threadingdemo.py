import threading
import time

exitFlag=0
#定义一个属于自己的线程继承threading.Thread类，
class myThread(threading.Thread):
    

    def __init__(self,threadID,name,counter):
        #一定要调用父类的__init__()方法
        super().__init__()
        self.threadID = threadID
        self.name   = name
        self.counter = counter

    def run(self):
        print("开始线程"+self.name)
        print_time(self.name,self.counter,5)
        print("结束线程"+self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s"%(threadName,time.ctime(time.time())))
        counter -=1

thread1 = myThread(1,"Thread - 1",1)
thread2 = myThread(2,"Thread - 2",2)
#开始线程
thread1.start()
thread2.start()
#等待至线程结束
thread1.join()
thread2.join()

print("退出主线程")

