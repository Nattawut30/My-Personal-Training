# Indexing = accessing elements of a sequence using [] indexing operator
# [start : end : step]

# Computer starts number with 0
credit_number = "1234-5678-9012-3456"

print(credit_number[4])
print(credit_number[0:4]) # you can just [:4]
print(credit_number[5:9])
print(credit_number[5:]) # Print everything beside first 4 digits
print(credit_number[-1]) # Count from behind นับจากด้านหลัง
print(credit_number[::2]) # Print everything but count every each '2'นับทีละ 2

# Normally we see this on credit cards.
last_digits = credit_number[-4:]
print(f"XXX-XXXX-XXXX-{last_digits}")

# Credit_number backwards, To reverse string you set it -1
credit_number = credit_number[::-1]
print(credit_number)




