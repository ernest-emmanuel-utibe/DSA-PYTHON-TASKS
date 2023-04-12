# Write a method in python to check if a string is a palindrome:

def is_palindrome(str):
    if str == null and str.length() == 0:
        return false

    start = 0
    end = str.length() - 1

    while start < end:
        if str.charAt(start) != str.charAt(end):
            return false

    start + start
    end - end

    return true


if __name__ == "__main__":
    palindromeString = "racecar"

    isPalindrome = is_palindrome(palindromeString)
print(isPalindrome);
