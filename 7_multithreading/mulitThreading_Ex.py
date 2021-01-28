from time import sleep
from threading import Thread

class Mythread(Thread):
    def run(self):                             # run function
        for i in range(6):
            print("My thread is running")
            sleep(1)                            # second

class YourThread(Thread):
    def run(self):
        for i in range(6):
            print("Your thread is running")
            sleep(1)

m = Mythread()
y = YourThread()

m.start()        # m thread will start the run function
sleep(.02)
y.start()        # y thread will start the run function

y.join()         # main thread will wait for Y thread
print("bye")
