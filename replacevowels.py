name = input("Enter your name: ")
result = ""
for ch in name:
    if ch.lower()in "aeiou":
        result = result +"z"
    else :
        result = result + ch
print ("New Name: ",result)            
