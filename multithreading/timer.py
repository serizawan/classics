import time
from threading import Thread

def timer(name, delay, repeat):
    print('Timer: ' + name + ' started')
    while repeat:
        time.sleep(delay)
        print(name + ': ' + str(time.ctime(time.time())))
        repeat -= 1
    print('Timer: ' + name + ' completed')

def main():
    t1 = Thread(target=timer, args=('Timer1', 1, 5))
    t2 = Thread(target=timer, args=('Timer2', 2, 5))
    t1.start()
    t2.start()
    print('Main completed')

if __name__ == '__main__':
    main()
