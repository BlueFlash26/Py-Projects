import time

def liftoff():
    for i in range(10, 0, -1):
        print(i, end=' ')
        time.sleep(1)
    print("\nLift off!")

liftoff()
