import time

# After 3 seconds, it's print value "Time's up!"
time.sleep(1)
print("TIME'S UP!")

# counting time by for loops
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60 # The modulus operator gives you the remainder of any division
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("HAPPY NEW YEARS!")

