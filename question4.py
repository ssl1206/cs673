import string

str1 = "absbc"
str2 = "absba"
str3 = "fdsaasdf"
str4 = "fgdsvxzca"

def is_palindrome(str):
    for i in (0,len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print(is_palindrome(str1))
print(is_palindrome(str2))
print(is_palindrome(str3))
print(is_palindrome(str4))