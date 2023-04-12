# Write a method in python to check if a string is a palindrome:

public
static
boolean
isPalindrome(String
str) {
if (str == null | | str.length() == 0)
{
return false;
}

int
start = 0;
int
end = str.length() - 1;

while (start < end) {
if (str.charAt(start) != str.charAt(end)) {
return false;
}
start + +;
end - -;
}

return true;
}

String
palindromeString = "racecar";
boolean
isPalindrome = isPalindrome(palindromeString);
System.out.println(isPalindrome);
