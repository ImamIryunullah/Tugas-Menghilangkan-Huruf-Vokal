x = ('a','i','u','e','o','A','I','U','E','O')
y = input("")
z = ""
for kata_kata in y:
    if kata_kata not in x:
        z += kata_kata
print (z)