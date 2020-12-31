def is_palindrome(word):
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False


    return True

if __name__ == "__main__":
    print(is_palindrome("racecar"))
