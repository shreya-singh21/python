#split inbuilt fuction
arn = "arn:aws:iam::123456789012:user/johndoe"

print(arn.split("/"))

#Add two strings - String Concatination
str1 ="Hello"
str2 ="World"

result = str1 + " " + str2
print(result)

#String Length
text = "python is awesome"
length = len(text)
print("Length of the string:",length)

#String Strip
text = " some spaces around "
stripped_text = text.strip()
print("stripped_text:",stripped_text)