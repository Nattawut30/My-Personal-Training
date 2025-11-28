# default arguments = A default value for certain parameters
#                   default is used when that arguments omitted
#                   make your function more flexible, reduces # of arguments
#                   1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# Ex.1
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))
print()

# Ex. 2
import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(30, 15)






