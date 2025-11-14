str1 = "HELLO"
str2 = "WORLD"

print("String 1:", str1)
print("String 2:", str2)

# FIX 1: Concatenate with a space added explicitly
str3 = str1 + " " + str2 

# FIX 2: Use an f-string (most common method today)
# str3 = f"{str1} {str2}"

blank=" "
str4 = str1+blank+str2
print(str4)
print("String 3:", str3)



newString = "Hello" * 3
print(newString)





str5="Hello"
str6="World"
print ("String 5:",str5)
print ("String 6:",str6)
str7=str5+str6*3
print("String 7:",str7)
str8=(str5+str6)*3
print ("String :", str8)