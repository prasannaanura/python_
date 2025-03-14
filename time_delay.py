import time
'''print("hi")
time.sleep(7)
#this takes 7 second to print
print("hi im delay")

time.sleep(4)

print('time is up!')'''


import time

mytime = int(input('Enter time in second: '))

for x in reversed(range(mytime,0,-1)):
    seconds = x % 60
    minuits = int(x / 60) % 60
    hour = int(x / 3600) 
    print(f'{hour:02}:{minuits:02}:{seconds:02}')
    time.sleep(1)
print("time's up!")