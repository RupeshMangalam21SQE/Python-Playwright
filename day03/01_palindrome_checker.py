# 1. Palindrome Checker
def is_palindrome(text):
    clean = "".join(text.lower().split())
    return clean == clean[::-1]
print(is_palindrome("A man a plan a canal Panama"))