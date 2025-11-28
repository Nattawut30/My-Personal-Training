# Compound Interest Calculator

principle = 0
rate = 0
time = 0

# When we reach to the while loops, the conditions is "false" from the beginning.
# We will never end up entering these while loops at the beginning
# So, we set them "True". True is a boolean.
# True = means this while loop will continue forever.
# Also, we need to add 'break' in it to get out of the while loops.

while True:
    principle =  float(input("Enter the principle: "))
    if principle < 0:
        print("principle can't be less than zero.")
    else:
        break # Break will break out of the loop

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero.")
    else:
        break # Break out of the loop

while True:
    time =  float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero.")
    else:
        break # Break out of the loop

# Result
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

