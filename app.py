def palindrome(str):
    reverse = str[::-1]

    return reverse == str


result = palindrome('racecar')
print(result)
