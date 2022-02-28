from threading import Thread
from time import sleep


def countdown_activity():
    for i in range(10, -1, -1):
        print(f"   COUNTDOWN {i}")
        sleep(1.5)
    print("   Thread ends.")

# Change to daemon=True and observe the different behaviour.
mythread = Thread(target=countdown_activity, daemon=False)
print("About to start thread...")
mythread.start()

for i in range(5):
    print(f"Main program counter {i}")
    sleep(0.4)

print("Main ends.")
