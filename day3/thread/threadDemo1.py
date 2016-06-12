import time
import _thread

def print_time(no,interval):
    cnt = 0
    while cnt<10:
        print("Thread:(%d) Time :%s\n"%(no,time.ctime()))
        time.sleep(interval)
        cnt+=1
    _thread.exit()

def test():
    _thread.start_new_thread(timer,(1,1,))
    _thread.start_new_thread(timer,(2,2,))
    
if __name__=="__main__":
    try:
        _thread.start_new_thread(print_time,(1,1))
        _thread.start_new_thread(print_time,(2,2))
    except:
        print("Error :程序出错了")
    while 1:
        pass
