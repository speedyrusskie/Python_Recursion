def isPalindrome(s):
    return isPalindromeHelper(s,0, len(s) - 1)
    
def isPalindromeHelper(s, low, high):
    if high <= low: #Base case
        return True
    elif s[low] != s[high]: #Base case 
        return False
    else:
        return isPalindromeHelper(s, low + 1, high - 1)

print(isPalindrome("noon"))
print(isPalindrome("moon"))