def per (str):
    str1 =""
    i=0
    while i<len(str):
        str1+=str[len(str)-1-i]
        i+=1
    return str1

print(per("Hello, world"))