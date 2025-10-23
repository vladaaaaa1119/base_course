a = int(input("AC:"))
b = int(input("AB:"))
c = int(input("BC:"))
d = [a, b, c]
result = "не существует"
for i in range(len(d)):
    if (a+b>=c) and (a+c>=b) and (b+c>=a):
        result = "существует"
    else:
        continue
   
print(result)