def is_palindrome(s):
    """
    Check if a string is a palindrome.
    Ignores spaces, punctuation, and case.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare with reversed string
    return cleaned == cleaned[::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "12321",
        "Was it a car or a cat I saw?"
    ]
    
    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")