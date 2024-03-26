import time

myTimer = int(input("Enter the time in sec: "))

for counter in range(myTimer, 0 , -1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")