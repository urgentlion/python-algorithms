def palindrome(str):
    reversed = str[::-1]
    return reversed == str


result = palindrome("racecar")
print(result)